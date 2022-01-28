[![Build Status](https://travis-ci.org/AineKiraboMbabazi/disease_diagnosis_with_Machine-Learning.svg?branch=diagnosis-api)](https://travis-ci.org/AineKiraboMbabazi/disease_diagnosis_with_Machine-Learning)
[![Coverage Status](https://coveralls.io/repos/github/AineKiraboMbabazi/disease_diagnosis_with_Machine-Learning/badge.svg?branch=diagnosis-api)](https://coveralls.io/github/AineKiraboMbabazi/disease_diagnosis_with_Machine-Learning?branch=diagnosis-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/1b4e5b23bea9dcb5f9d4/maintainability)](https://codeclimate.com/github/AineKiraboMbabazi/disease_diagnosis_with_Machine-Learning/maintainability)


# Disease diagnosis with pandas
# Animal disease diagnosis
The diagnosis api enables users search for details of a particular animal disease, the details include the symptoms,causes and treatment for a given disease. 

Another feature supported by the api is the ability to retrieve an animal disease based on the symptoms specified by the user.

This api is going to be a backend for the diagnosis web app. Currently has support for rabbit diseases.


# Getting started #
create a directory on your computer by doing the following 
- Open the terminal, for linux
```
 Ctrl+Alt+ T
 ```
 - Create a directory for the project by typing the following in your terminal
 ```
 mkdir projectname
 ```
 - Change into the directory created by using the following command
 ```cd projectname
 ```
## Clone the repository
After creating the directory, the next step is to clone this project by using the following command
```
$ git clone (https://github.com/AineKiraboMbabazi/disease_diagnosis_with_Machine-Learning.git)

```

## Preprequisites ##
Install requirements
```
pip3 install -r requirements.txt
```
make sure that you have  python3 and postman installed on your computer
To install postman
For linux
```
snap install postman
```
Follow the link for windows installation
```
https://www.softwaretestingmaterial.com/install-postman/
```

# Running the project #
To run this project, 
- Navigate to the directory where the project was cloned.
run 
```
    python3 run.py
```
-Copy the link from the terminal and paste it in postman. This should load the index page

## Features

|Endpoint   |  HTTP Method  |CRUD Method   |Result   |  
|---|---|---|---|
| / |GET   |INDEX   |  Loads the home page |
| /index  |GET   |INDEX   |  Loads the home page |
| /api/v1/diseases/search?file_name =rabbit_diseases.xls&search_params=['nasal discharge']  |GET   |READ  |  Search disease by symptoms  | 
| /api/v1/diseases/details?file_name =rabbit_diseases.xls&disease_name=snuffles  |GET   |READ   |   Get disease details|

## Tests 
To run tests
```
python3 -m unittest
```
## Tech/framework used

<b>Built with</b>
- [Flask](http://flask.pocoo.org/docs/1.0/)
- [Python3](https://docs.python.org/3/)
- [Pandas](https://pandas.pydata.org/)

## Author
Software Engineer: Ainekirabo Mbabazi
#### Developer Stack
Python, Flask, Django


## License

MyFarm © [Ainekirabo Mbabazi]()
