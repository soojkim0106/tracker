from flask import request, make_response, jsonify
from flask_restful import Resource
from config import app, db, api

import os

from models.goal import Goal

STATUS = ["In Progress", "Not Started", "Completed"]


@app.route("/")
def index():
    return "<h1>Welcome to the Task API</h1>"


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


class GoalById(Resource):
    def get(self, id):
        if not (goal := Goal.query.get(id)):
            return {"message": "Goal not found"}, 404
        return goal.to_dict(), 200

    def patch(self, id):
        if not (goal := Goal.query.get(id)):
            return {"message": "Goal not found"}, 404
        try:
            data = request.get_json()
            goal = Goal.query.get(id)
            
            for attr in data:
                setattr(goal, attr, data[attr])
            if "status" in data and data["status"] in STATUS:
                goal.status = data["status"]
            db.session.commit()
            return goal.to_dict(), 202
        except Exception as e:
            db.session.rollback()
            return {"message": "Something went wrong", "error": str(e)}, 400

    def delete(self, id):
        try:
            if not (goal := Goal.query.get(id)):
                return {"message": "Goal not found"}, 404
            db.session.delete(goal)
            db.session.commit()
            return {"message": "Goal deleted"}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "Something went wrong", "error": str(e)}, 400


api.add_resource(Goals, "/goals")
api.add_resource(GoalById, "/goals/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
