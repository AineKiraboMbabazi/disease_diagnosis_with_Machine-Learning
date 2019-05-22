import unittest

from diagnosis_api.controllers.search_disease_by_syptoms import Search_disease_by_symptoms
# diagnosis_api/dataset

class TestSearchDiseaseBySymptoms(unittest.TestCase):

    def setUp(self):
        self.search_with_invalid_file = Search_disease_by_symptoms('rabbit.txt',['depression','anaemia','pale mucous Membrane','mucous in feaces','Blood in feaces'])
        self.void_search = Search_disease_by_symptoms('rabbit_diseases.xls',['nothing'])
        self.search = Search_disease_by_symptoms('rabbit_diseases.xls',['Scabby Crusty area At the base of the ear'])
        self.search_list = Search_disease_by_symptoms('rabbit_diseases.xls',['diarrhoea'])
        self.search_in_nonexistent_file= Search_disease_by_symptoms('rabbit_diseases.txt',['Scabby '])
        


    def test_can_successfully_get_disease_by_symptoms(self):
        disease =  self.search.search_disease_by_symptoms()
        self.assertIsInstance(disease,dict)
        disease =  self.search_list.search_disease_by_symptoms()
        self.assertIsInstance(disease,list)

    def test_symptoms_doesnt_match_any_disease(self):
        disease =  self.void_search.search_disease_by_symptoms()
        self.assertIsInstance(disease,dict)
        self.assertEqual(disease,{'message':'Disease with those symptoms doesnot exist'})


    def test_cant_successfully_get_disease_by_symptoms_for_nonexistent_file(self):
        details =  self.search_in_nonexistent_file.search_disease_by_symptoms()
        self.assertIsInstance(details,dict)
        self.assertEqual(details,{'message':'File with that name doesnot exist'})

    
    def test_cant_successfully_get_disease_by_symptoms_for_nonexcel_file(self):
        details = self.search_with_invalid_file.search_disease_by_symptoms()
        self.assertIsInstance(details,dict)
        self.assertEqual(details,{'message':'Dataset file format not supported, only excel files are accepted'})


    def tearDown(self):
        self.disease_details = None