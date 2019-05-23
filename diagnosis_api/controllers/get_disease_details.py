import pandas as pd
import os
from flask import jsonify


class DiseaseDetails:
    """
    Disease details model that defines the disease_details
    """

    def __init__(self, file_name, disease_name):
        self.file_name = file_name
        # convert disease name to lower case for uniformity
        self.disease_name = disease_name.lower()

    def load_disease_file(self):
        """
        load_disease_file function loads the disease excel file
        : return diseases dataframe:
        """

        file = pd.read_excel("diagnosis_api/dataset/{}".format(self.file_name))

        #  convert to dataframe
        df = pd.DataFrame(file)

        # autofill empty spaces with 0
        data = df.fillna(value=0)

        return data, file, df

    def get_disease_detail_param_details(self, query_string):
        """
        gets the details of causes,symptoms,treatment for a particular disease
        : param causes or symptoms or treatment :
        """
        # group data by disease
        disease_grouped_data = (
            self.load_disease_file()[0]
            .groupby("Disease")
            .apply(lambda g: pd.Series(g[query_string].values))
            .rename(columns=lambda x: "query_string%s" % x)
        )
        causes, symptoms, Treatments = [], [], []

        for row in disease_grouped_data[self.disease_name]:
            if (row != 0) & (query_string == "Causes"):
                causes.append(row)

            if (row != 0) & (query_string == "Symptoms"):
                symptoms.append(row)

            if (row != 0) & (query_string == "Treatment"):
                Treatments.append(row)

        return causes, symptoms, Treatments, disease_grouped_data

    def get_disease_details(self):
        """
        Get disease details
        : Return disease details :

        """
        # load disease file
        file_name = self.file_name
        basepath = "diagnosis_api/dataset/"
        files = []
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                files.append(entry)

        if file_name.lower() not in files:
            return {"message": "File with that name doesnot exist"}

        if not file_name.lower().endswith((".xls", ".xlsx")):
            return {
                "message": "Dataset file format not supported, only excel files are accepted"
            }

        disease_list = []

        for idx, row in self.load_disease_file()[0]["Disease"].items():
            disease_list.append(row)

        if self.disease_name not in disease_list:
            return {"message": "Disease with that name doesnot exist"}

        # disease Causes
        causes = self.get_disease_detail_param_details("Causes")[0]

        # disease symptoms
        symptoms = self.get_disease_detail_param_details("Symptoms")[1]

        # disease Treatment
        Treatments = self.get_disease_detail_param_details("Treatment")[2]

        disease_details = {
            "Disease_Name": self.disease_name,
            "Causes": causes,
            "Symptoms": symptoms,
            "Treatment": Treatments,
        }
        return {"disease_details": disease_details}
