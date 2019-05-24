import ast
from flask import request, jsonify
from diagnosis_api import app
from ..controllers.search_disease_by_syptoms import SearchDiseaseBySymptoms
from ..controllers.get_disease_details import DiseaseDetails

import datetime


"""Endpoint for the index page"""


@app.route("/index")
@app.route("/")
def index():
    return jsonify(
        {"message": "Welcome to disease diagnosis API with pandas"}), 200


"""
    Endpoint for getting diseases by symptoms
"""


@app.route("/api/v1/diseases/search", methods=["GET"])
def search_disease_by_sypmtoms():
    """
        function to get disease by sypmtoms
    """

    args = request.args.to_dict()
    file_name = args["file_name "]
    search_params_api = args["search_params"]
    search_params = ast.literal_eval(search_params_api)
    search = SearchDiseaseBySymptoms(file_name, search_params)
    result = search.search_disease_by_symptoms()
    return jsonify({"disease": result}), 200


@app.route("/api/v1/diseases/details", methods=["GET"])
def get_disease_details():
    """
        function to create a association
    """
    args = request.args.to_dict()
    file_name = args["file_name "]
    disease_name = args["disease_name"]
    search = DiseaseDetails(file_name, disease_name).get_disease_details()
    return jsonify({"disease_details": search}), 200
