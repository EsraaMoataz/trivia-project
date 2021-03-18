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
##### -General:

###### - Returns all questions,all categories,lengtht of all questions and success.

###### - Result are paginated in group of 10.Include a request argument to choose page number ,starting from 1.
##### -Sample: `curl http://127.0.0.1:5000/questions`

`{

    "categories": {
    
        "1": "Science",
        
        "2": "Art",
        
        "3": "Geography",
        
        "4": "History",
        
        "5": "Entertainment",
        
        "6": "Sports"
        
    },
    
    "current_category": null,
    
    "questions": [
    
        {
            "answer": "Maya Angelou",
            
            "category": 4,
            
            "difficulty": 2,
            
            "id": 5,
            
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            
        },
        
        {
        
            "answer": "Brazil",
            
            "category": 6,
            
            "difficulty": 3,
            
            "id": 10,
            
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            
        },
        
        {
            "answer": "George Washington Carver",
            
            "category": 4,
            
            "difficulty": 2,
            
            "id": 12,
            
            "question": "Who invented Peanut Butter?"
            
        },
        
        {
        
            "answer": "Lake Victoria",
            
            "category": 3,
            
            "difficulty": 2,
            
            "id": 13,
            
            "question": "What is the largest lake in Africa?"
            
        },
        
        {
        
            "answer": "The Palace of Versailles",
            
            "category": 3,
            
            "difficulty": 3,
            
            "id": 14,
            
            "question": "In which royal palace would you find the Hall of Mirrors?"
            
        },
        
        {
        
            "answer": "Agra",
            
            "category": 3,
            
            "difficulty": 2,
            
            "id": 15,
            
            "question": "The Taj Mahal is located in which Indian city?"
            
        },
        
        {
        
            "answer": "Escher",
            
            "category": 2,
            
            "difficulty": 1,
            
            "id": 16,
            
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
            
        },
        
        {
        
            "answer": "Mona Lisa",
            
            "category": 2,
            
            "difficulty": 3,
            
            "id": 17,
            
            "question": "La Giaconda is better known as what?"
            
        },
        
        {
        
            "answer": "One",
            
            "category": 2,
            
            "difficulty": 4,
            
            "id": 18,
            
            "question": "How many paintings did Van Gogh sell in his lifetime?"
            
        },
        
        {
        
            "answer": "Jackson Pollock",
            
            "category": 2,
            
            "difficulty": 2,
            
            "id": 19,
            
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
       
       }
       
    ],
    
    "success": true,
    
    "total_questions": 18
    
}`

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
