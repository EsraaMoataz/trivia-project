import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from models import *

QUESTIONS_PER_PAGE = 10
def pagination_questions(request,questions):
  page=request.args.get('page',1,type=int)
  start=(page-1)*QUESTIONS_PER_PAGE
  end=start+QUESTIONS_PER_PAGE
  questions_formate=[Q.format() for Q in questions]
  current_questions=questions_formate[start:end]
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  
  #@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  CORS(app, resources={r"/api/*" :{"origins":"*"}})
  

  #@TODO: Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
    response.headers.add('Access_Control_Allow_Headers','Content_Type,Authorization')
    response.headers.add('Access_Control_Allow_Methods','GET,POST,PATCH,DELETE,OPTIONS')
    return response
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    if request.method!='GET':
      abort(405)
    #formated_categories=[]
    categories=Category.query.all()
    '''all_categories=[c.format() for c in categories]
    for category in all_categories:
        formated_categories.append({category['id']:category['type']})'''
    return jsonify({
      'success' : True,
      #"categories" : formated_categories, 
      "categories": {category.id: category.type for category in categories}    
      #"No of categories" : len(all_categories)

    })


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. '''
  @app.route('/questions')
  def get_questions():
    questions=Question.query.order_by(Question.id).all()
    categories=Category.query.order_by(Category.type).all()
    #categories_formate=[C.format() for C in categories]
    current_questions=pagination_questions(request,questions)
    categories_dict = {}
    for category in categories:
      categories_dict[category.id] = category.type
    if len(current_questions)==0:
      abort(404)
    
    return jsonify(
      {
        'success':True,
        'questions':current_questions,
        'total_questions':len(questions),
        #'categories':categories_formate,
        #'categories': {category.id: category.type for category in categories},
        'categories':categories_dict,
        'current_category': None
        
        #'NO of All questions':len(questions),
        #'NO of questions per page':len(current_questions)
        
      }
    )
  '''
  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/<int:question_id>',methods=['DELETE'])
  def delete_question(question_id):
    if request.method!='DELETE':
      abort(405)
    try:
      Q=Question.query.filter(Question.id==question_id).one_or_none()
      print (Q)
      '''if Q is None:
        abort(404)'''
      
      Q.delete()
      questions=Question.query.order_by(Question.id).all()
      #current_questions=pagination_questions(request,questions)
      return jsonify({
        'success':True,
        #'question_id':question_id,
        'deleted':question_id,
        #'questions per page':current_questions,
        #"no of all questions":len(questions)
      })
    except:
      db.session.rollback()
      print("question hasn't been deleted")
      abort(404)
    finally:
      db.session.close()
    




  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions',methods=['POST'])
  def add_questions():
    print("##########################333333333")
    if request.method!='POST':
      abort(405)
    try:
      body=request.get_json()
      print(body)
      question=body.get('question',None)
      answer=body.get('answer',None)
      category=body.get('category',None)
      difficulty_rate=body.get('difficulty',None)
      new_question=Question(question=question,answer=answer,category=category,difficulty=difficulty_rate)
      new_question.insert()
      questions=Question.query.order_by(Question.id).all()

      return jsonify({
      'success':True,
      'question': new_question.question,
      'answer':new_question.answer,
      'difficulty':new_question.difficulty,
      'category':new_question.category
      
    })

    except:
      db.session.rollback()
      abort(422)
    finally:
      db.session.close()
    
  '''@app.route('/test' ,methods=['POST'])
  def test():
    #body=request.get_json()
    #print(body)
    question=request.get_json()["test1"]
    print(question)
    return jsonify({
      "test_success" :question
    })'''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/search',methods=['POST'])
  def search():
    if request.method!='POST':
      abort(405)
    try:
      #entered_search_term=request.args.get('search_term',None,type=str)
      body=request.get_json()
      entered_search_term=body.get('searchTerm',None)
      search_questions=Question.query.filter(Question.question.ilike(f'%{entered_search_term}%')).all()
      all_searched_questions=[s.format() for s in search_questions]
      return jsonify({
        'success': True,
        'questions':all_searched_questions,
        'total_questions': len(all_searched_questions),
        'current_category':None
      })
      
    except:
        abort(422)
    finally:
        db.session.close()


  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:catagory_id>/questions')
  def get_spcefic_questions(catagory_id):
    if request.method!='GET':
      abort(405)
    specific_questions=Question.query.filter(Question.category==catagory_id).all()
    final_questions=[q.format() for q in specific_questions]
    return jsonify({
      'success':True,
      'questions':final_questions,
      'total_questions':len(final_questions),
      'category':catagory_id

    })


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quiz', methods= ['POST'])
  def play_quiz():
    try:
      body= request.get_json()
      
      if not ('quiz_category' in body and 'previous_questions' in body):
                abort(422)

      category= body.get('quiz_category', None)
      previous_questions_ids= body.get('previous_questions', None)
      if ((category is None) or (previous_questions_ids is None)):
            abort(400)

      if category['type'] == 'click':
        questions_per_said_category=Question.queryfilter(Question.id.notin_((previous_questions_ids))).all()
      else:
        questions_per_said_category=Question.query.filter(Question.category==category['id']).filter(Question.id.notin_((previous_questions_ids))).all()
      
      total=len(questions_per_said_category)


      current_question = questions_per_said_category[random.randrange(
                0, len(questions_per_said_category))].format() if len(questions_per_said_category) > 0 else None

      if (len(previous_questions_ids) == total):
                return jsonify({
                    'success': True
                })

      return jsonify({
        'success' : True,
        'question' : current_question,
        'question-id' : current_question['id'],
        'category-id':category['id'],

       })
    except:
      abort(422)
    finally:
      db.session.close()





  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success' : False,
      'error' : 404,
      'message': 'Not Found'
    }),404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success' : False,
      'error' : 422,
      'message' : "unprocessable"
    }),422

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success' : False,
      'error' : 405,
      'message' : 'Method Not Allowed'
    }),405
  
  return app

    
