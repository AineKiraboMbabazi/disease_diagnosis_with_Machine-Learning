import os
import pandas as pd


def load_file(file_name):
    files = pd.read_excel(
        "diagnosis_api/dataset/{}".format(file_name)
    )
    return files


def check_disease_file(file_name):
    # check if the file exists
    basepath = "diagnosis_api/dataset/"
    files = []
    message = None
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            files.append(entry)

    if file_name.lower() not in files:

        message = {"message": "File with that name doesnot exist"}

    # check for non excel files
    if not file_name.lower().endswith((".xls", ".xlsx")):

        message = {
            "file_format": os.path.splitext(file_name)[1],
            "message": "Dataset file format not supported, only excel files are accepted"}

    return message
