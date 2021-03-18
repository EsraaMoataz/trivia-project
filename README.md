# Full Stack API
## Trivia-API
Trivia is full stack API that allows you to see all questions based on thier categories or not, search for question and play a quiz containing difference questions

  1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
  2. Delete questions.
  3. Add questions and require that they include question and answer text.
  4. Search for questions based on a text query string.
  5. Play the quiz game, randomizing either all questions or within a specific category.


## Getting started

### Pre-requisites and local development

Developers using this project should already have python3,pip and node installed in thier local machines

#### Backend
The ./backend directory contains a partially completed Flask and SQLAlchemy server.

From the backend folder run pip install `requirements.txt`. All required package included in requirements file.

To run the server, execute:

`export FLASK_APP=flaskr

 export FLASK_ENV=development
 
 flask run`
 
 The application is run on  `http://127.0.0.1:5000/`by default that is the localhost.
#### Frontend
The ./frontend directory contains a complete React frontend to consume the data from the Flask server. 

From the frontend folder run the following commands to start the client:

  `npm install //only once to install dependencies

   npm start`

By default, the frontend run on localhost `http://localhost:3000` 
## Testing
In order to run tests navigate to the backend folder and run the following conmmands:

  `dropdb trivia_test

   createdb trivia_test

   psql trivia_test < trivia.psql

   python test_flaskr.py`

## API References
### Getting Started
- Base URL:This application can only be run locally and is not hosted as a base URL.The backend app is hosted as the default `http://127.0.0.1:5000/` .

- Authentication:This version of application doen't require authentication for API keys.
### Error Handling
Errors are returned as JSON objects in the following formate:


    `{
      "success" : False,
      
      "error" : 404,
      
      "message": "Not Found"
    }`
    
 
This API uses 3 types of error types when requests fail:

- 404: Bad Request
- 422: Unprocessable
- 405: Method not allowed

### EndPoints
#### GET/questions
##### - General:

##### - Sample:


#### GET/categories
##### - General:

##### - Sample:
#### DELETE/<int:question_id>
##### - General:

##### - Sample:
#### POST/questions
##### - General:

##### - Sample:
#### POST/search
##### - General:

##### - Sample:
#### GET/categories/<int:catagory_id>/questions
##### - General:

##### - Sample:
#### GET/quiz/<int:category_id>/<int:question_id>
##### - General:

##### - Sample:

###
## Authors
