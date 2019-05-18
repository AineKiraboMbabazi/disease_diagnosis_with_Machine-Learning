import pandas as pd 
import os


class Disease_details:
    """
    Disease details model that defines the disease_details
    """

    def __init__(self,file_name,disease_name):
        self.file_name = file_name
        # convert disease name to lower case for uniformity
        self.disease_name = disease_name.lower()
        self.causes = []
        self.symptoms = []
        self.Treatments = []

    def load_disease_file(self):
        """ 
        load_disease_file function loads the disease excel file
        : return diseases dataframe:
        """

        load_disease_files = pd.read_excel('diagnosis_api/dataset/{}'.format(self.file_name))
        
        
        #  convert to dataframe
        df = pd.DataFrame(load_disease_files)

        # autofill empty spaces with 0
        data = df.fillna(value = 0)
        return data


    def get_disease_detail_param_details(self,query_string):
        """ 
        gets the details of causes,symptoms,treatment for a particular disease
        : param causes or symptoms or treatment :
        
        """

       
        # check for non excel files
        
        data = self.load_disease_file()
        
        # group data by disease
        disease_grouped_data = data.groupby('Disease').apply(lambda g: pd.Series(g[query_string].values)).rename(columns=lambda x: 'query_string%s' % x)
       
        
        # if not isinstance(disease_grouped_data[self.disease_name], pd.Series):
        #     print('disease doesnt exist')
        #     return({'message':'Disease with that name doesnot exist'})

        for  row in disease_grouped_data[self.disease_name]: 
            if ((row != 0) &( query_string == 'Causes')):
                self.causes.append(row)

            if ((row != 0) & (query_string == 'Symptoms')):
                self.symptoms.append(row)

            if ((row != 0) & (query_string == 'Treatment')):
                self.Treatments.append(row) 



    def get_disease_details(self): 
        """ 
        Get disease details
        : Return disease details :

        """
        # load disease file
        file_name = self.file_name
        basepath = 'diagnosis_api/dataset/'
        files = []
        
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                
                files.append(entry)
        # print(file_name)
        if file_name.lower() not in files:
            
            return({'message':'File with that name doesnot exist'})
                
        if (not file_name.lower().endswith(('.xls','.xlsx'))):
            
            return({'message':'Dataset file format not supported, only excel files are accepted'})

        # disease Causes
        self.get_disease_detail_param_details('Causes') 
        
        # disease symptoms
        self.get_disease_detail_param_details('Symptoms') 
        
        # disease Treatment
        self.get_disease_detail_param_details('Treatment')
        
        disease_details = {
            'Disease_Name':self.disease_name,
            'Causes':self.causes,
            'Symptoms':self.symptoms,
            'Treatment':self.Treatments
        }
        return( disease_details)


