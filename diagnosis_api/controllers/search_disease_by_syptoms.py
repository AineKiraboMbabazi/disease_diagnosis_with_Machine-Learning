import pandas as pd
import os


# from get_disease_details import Disease_details

class Search_disease_by_symptoms:

    def __init__(self, file_name,search_params):
        self.file_name = file_name
        self.search_params = search_params
        self.disease = None
        self.query_list = []

    def convert_string_to_lower(self):
        """
        
        This function converts the search query list parameters into lower case
        : returns a list of lower case query string parameters :
         
        """
        for i in self.search_params:
            self.query_list.append(i.lower())

        return (self.query_list)

    def search_disease_by_symptoms(self):
        """

        This function searches the disease by symptoms
        : returns a list of possible diseases if the symptoms are shared across multiple diseases. 
        or disease if the symptom occur in a single disease or 
        message if the sypmtoms donot match any of the diseases :

        """
        
        # check if the file exists
        basepath = 'diagnosis_api/dataset/'
        files = []
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                files.append(entry)

        if self.file_name.lower() not in files:
            return({'message':'File with that name doesnot exist'})
                
        
        # check for non excel files

        if ( not self.file_name.lower().endswith(('.xls','.xlsx'))):

            return({'message':'Dataset file format not supported, only excel files are accepted'})
        
        
        # load disease file
        diseases = pd.read_excel('diagnosis_api/dataset/{}'.format(self.file_name))
       
        # Fill the missing values with 0
        data = diseases.fillna(value = 0)
        
        # Filter data to focus on diseases and symptoms
        test1 =  data[['Disease','Symptoms']]

        # Search in the symptoms for specified disease symptoms
        
        subsetDataFrame = test1[test1['Symptoms'].isin(self.convert_string_to_lower()) ]
        
        # if the symptoms occur in multiple diseases
        if len(subsetDataFrame.index ) > 1:
            # Group all similar disease together and count number of occurrance of each disease
            dups_diseases = subsetDataFrame.pivot_table(index=['Disease'], aggfunc='size')
            
            # returns the maximum number of duplications
            maximum_disease_occurance_count = dups_diseases.max()

            # create list for most likely disease
            possible_diseases = []
            for idx,row in dups_diseases.items():
                if row == maximum_disease_occurance_count:
                    possible_diseases.append(idx)
                self.disease = possible_diseases
            
            return (self.disease)

        # if the symptom occurs in one disease. 
        self.disease = subsetDataFrame['Disease'].sum()
        # check if the search didnt return any results
        if self.disease == 0:
            return ({'message':'Disease with those symptoms doesnot exist'})

        return(self.disease)
        
        
        

# # testing the operation of the class
# search = Search_disease_by_symptoms('rabbit_diseases.xlms',['depression','anaemia','pale mucous Membrane','mucous in feaces','Blood in feaces'])
# print(search.search_disease_by_symptoms())
# search = Search_disease_by_symptoms('rabbit_diseases.xls',['Scabby Crusty area At the base of the ear'])
# print(search.search_disease_by_symptoms())
# search = Search_disease_by_symptoms('rabbit_diseases.xls',['Scabby '])
# print(search.search_disease_by_symptoms())
# search = Search_disease_by_symptoms('rabbit.txt',['Scabby '])
# print(search.search_disease_by_symptoms())
