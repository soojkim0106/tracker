from flask import request, make_response, jsonify
from flask_restful import Resource
from config import app, db, api

import os

from models.goal import Goal

STATUS = ["In Progress", "Not Started", "Completed"]

@app.route("/")
def index():
    return '<h1>Welcome to the Task API</h1>'

class Goals(Resource):
    def get(self):
        try:
            goals = [goal.to_dict() for goal in Goal.query.all()]
            
            return goals, 200
        except Exception as e:
            return {"message": "Something went wrong", "error": str(e)}, 404
        
    
    def post(self):
        try:
            data = request.get_json()
            new_goal = Goal(**data)
            
            db.session.add(new_goal)
            db.session.commit()
            return new_goal.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": "Something went wrong", "error": str(e)}, 400
