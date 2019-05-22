import unittest
from flask import json
from diagnosis_api.routes import disease_diagnosis
from diagnosis_api import app


class TestApiRoutes(unittest.TestCase):

    def setUp(self):
        self.app_client = app.test_client()
    
    def test_index(self):

        index = self.app_client.get("/index", content_type="application/json")
        self.assertEqual(index.status_code, 200)
        response = json.loads(index.data)
        self.assertEqual(response['message'], 'Welcome to disease diagnosis API with pandas')

    def test_index1(self):
     
        index = self.app_client.get("/", content_type="application/json")
        self.assertEqual(index.status_code, 200)
        response = json.loads(index.data)
        self.assertEqual(response['message'], 'Welcome to disease diagnosis API with pandas')

    def test_api_gets_disease_details(self):
        disease_details = self.app_client.get("api/v1/get_disease_details?file_name =rabbit_diseases.xls&disease_name=snuffles", content_type="application/json")
        self.assertEqual(disease_details.status_code, 200)
        response = json.loads(disease_details.data)
        self.assertIsInstance(response,dict)

    def test_api_searches_disease_by_symptoms(self):
        disease = self.app_client.get("api/v1/get_disease_by_sypmtoms?file_name =rabbit_diseases.xls&search_params=['nasal discharge']", content_type="application/json")
        self.assertEqual(disease.status_code, 200)
        response = json.loads(disease.data)
        self.assertIsInstance(response,dict)


    def tearDown(self):
        self.app_client = None