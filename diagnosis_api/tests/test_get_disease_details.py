import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal, assert_equal


from diagnosis_api.controllers.get_disease_details import DiseaseDetails


class GetDiseaseDetails(unittest.TestCase):
    """

    Unittests for the get disease details class

    """

    def setUp(self):
        self.load_disease_files = pd.read_excel(
            "diagnosis_api/dataset/{}".format("rabbit_diseases.xls")
        )
        self.df = pd.DataFrame(self.load_disease_files)
        self.data = self.df.fillna(value=0)
        self.disease_details = DiseaseDetails(
            file_name="rabbit_diseases.xls", disease_name="tyzzers_disease"
        )
        self.non_existent_disease_details = DiseaseDetails(
            file_name="rabbit_diseases.xls", disease_name="malaria"
        )
        self.disease_with_non_existent_filename = DiseaseDetails(
            file_name="rabbit.xls", disease_name="snuffles"
        )
        self.disease_with_non_excel_file = DiseaseDetails(
            file_name="rabbit.txt", disease_name="tyzzers_disease"
        )

    def test_can_successfully_get_disease_details(self):
        details = self.disease_details.get_disease_details()
        self.assertIsInstance(details, dict)

    def test_load_disease_file_returns_dataframe(self):
        details = self.disease_details.load_disease_file()
        self.assertIsInstance(details, tuple)

    def test_load_disease_file_contains_dataframe(self):
        details = self.disease_details.load_disease_file()
        assert_frame_equal(details[0], self.data)

    def test_load_disease_file_contains_pandas_object(self):
        details = self.disease_details.load_disease_file()
        assert_equal(details[1], self.load_disease_files)

    def test_load_disease_file_contains_dataframe_with_spaces_filled_with_zero(
            self):
        details = self.disease_details.load_disease_file()
        assert_equal(details[2], self.df)

    def test_get_disease_detail_param_details_contains_causes(self):
        details = self.disease_details.get_disease_detail_param_details(
            "Causes")
        self.assertIsInstance(details[0], list)

    def test_get_disease_detail_param_details_contains_symptoms(self):
        details = self.disease_details.get_disease_detail_param_details(
            "Symptoms")
        self.assertIsInstance(details[1], list)

    def test_get_disease_detail_param_details_contains_treatment(self):
        details = self.disease_details.get_disease_detail_param_details(
            "Treatment")
        self.assertIsInstance(details[2], list)

    def test_get_disease_detail_param_details_contains_series_of_grouped_data(
            self):
        details = self.disease_details.get_disease_detail_param_details(
            "Treatment")
        self.assertEqual(details[3].size, 70)

    def test_cant_successfully_get_disease_details_for_nonexistent_file(self):
        details = self.disease_with_non_existent_filename.get_disease_details()
        self.assertIsInstance(details, dict)
        self.assertEqual(
            details, {
                "message": "File with that name doesnot exist"})

    def test_cant_successfully_get_disease_details_for_nonexcel_file(self):
        details = self.disease_with_non_excel_file.get_disease_details()
        self.assertIsInstance(details, dict)
        self.assertEqual(
            details, {
                "message": "Dataset file format not supported, only excel files are accepted"}, )

    def test_cant_successfully_get_disease_details_for_nonexistent_disease(
            self):
        details = self.non_existent_disease_details.get_disease_details()
        self.assertIsInstance(details, dict)
        self.assertEqual(
            details, {
                "message": "Disease with that name doesnot exist"})

    def tearDown(self):
        self.disease_details = None
