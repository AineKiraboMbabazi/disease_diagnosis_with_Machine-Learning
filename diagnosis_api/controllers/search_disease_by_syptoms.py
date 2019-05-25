import pandas as pd

from flask import jsonify
from .load_dataset import load_file, check_disease_file


class SearchDiseaseBySymptoms:
    def __init__(self, file_name, search_params):
        self.file_name = file_name
        # parse the string list returned by the api to a list by using the ast
        # library
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

        return self.query_list

    def search_disease_by_symptoms(self):
        """
        This function searches the disease by symptoms
        : returns a list of possible diseases if the symptoms are shared across
        multiple diseases. or disease if the symptom occur in a single disease
        or message if the sypmtoms donot match any of the diseases :
        """

        # check if the file exists
        check_file = check_disease_file(self.file_name)
        if not check_file:
            # load disease file
            diseases = load_file(self.file_name)

            # Fill the missing values with 0
            data = diseases.fillna(value=0)

            # Filter data to focus on diseases and symptoms
            test1 = data[["Disease", "Symptoms"]]

            # Search in the symptoms for specified disease symptoms

            subsetDataFrame = test1[
                test1["Symptoms"].isin(self.convert_string_to_lower())
            ]

            # if the symptoms occur in multiple diseases
            if len(subsetDataFrame.index) > 1:
                # Group all similar disease together
                #  count number of occurrance of each disease
                dups_diseases = subsetDataFrame.pivot_table(
                    index=["Disease"], aggfunc="size"
                )

                # returns the maximum number of duplications
                maximum_disease_occurance_count = dups_diseases.max()

                # create list for most likely disease
                possible_diseases = []
                for idx, row in dups_diseases.items():
                    if row == maximum_disease_occurance_count:
                        possible_diseases.append(idx)

                    self.disease = possible_diseases

                return self.disease

            # if the symptom occurs in one disease.
            self.disease = subsetDataFrame["Disease"].sum()

            # check if the search didnt return any results
            if self.disease == 0:
                return {"message": "Disease with those symptoms doesnot exist"}

            return {"disease": self.disease}

        return check_file
