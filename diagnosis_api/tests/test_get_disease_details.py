import unittest

from diagnosis_api.controllers.get_disease_details import Disease_details
# diagnosis_api/dataset

class GetDiseaseDetails(unittest.TestCase):

    def setUp(self):
        self.disease_details = Disease_details('rabbit_diseases.xls','tyzzers_disease')
        self.non_existent_disease_details = Disease_details('rabbit_diseases.xls','malaria')
        self.disease_with_non_existent_filename = Disease_details('rabbit.xls','snuffles')
        self.disease_with_non_excel_file = Disease_details('rabbit.txt','tyzzers_disease')

    def test_can_successfully_get_disease_details(self):
        details =  self.disease_details.get_disease_details()
        self.assertIsInstance(details,dict)


    def test_cant_successfully_get_disease_details_for_nonexistent_file(self):
        details =  self.disease_with_non_existent_filename.get_disease_details()
        self.assertIsInstance(details,dict)
        self.assertEqual(details,{'message':'File with that name doesnot exist'})

    
    def test_cant_successfully_get_disease_details_for_nonexcel_file(self):
        details =  self.disease_with_non_excel_file.get_disease_details()
        self.assertIsInstance(details,dict)
        self.assertEqual(details,{'message':'Dataset file format not supported, only excel files are accepted'})

        
    # def test_cant_successfully_get_disease_details_for_nonexistent_disease(self):
    #     details =  self.non_existent_disease_details.get_disease_details()
    #     self.assertIsInstance(details,dict)
    #     self.assertEqual(details,{'message':'Disease with that name doesnot exist'})
    
    def tearDown(self):
        self.disease_details = None