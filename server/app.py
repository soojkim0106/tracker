from flask import request, make_response, jsonify
from flask_restful import Resource
from config import app, db, api

import os

from models.task import Task

STATUS = ["In Progress", "Not Started", "Completed"]


@app.route("/")
def index():
    return "<h1>Welcome to the Task API</h1>"


class Tasks(Resource):
    def get(self):
        try:
            tasks = [task.to_dict() for task in Task.query.all()]

            return tasks, 200
        except Exception as e:
            return {"message": "Something went wrong", "error": str(e)}, 404

    def post(self):
        try:
            data = request.get_json()
            new_task = Task(**data)

            db.session.add(new_task)
            db.session.commit()
            return new_task.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": "Something went wrong", "error": str(e)}, 400


class TaskById(Resource):
    def get(self, id):
        if not (task := Task.query.get(id)):
            return {"message": "Task not found"}, 404
        return task.to_dict(), 200

    def patch(self, id):
        if not (task := Task.query.get(id)):
            return {"message": "Task not found"}, 404
        try:
            data = request.get_json()
            task = Task.query.get(id)
            
            for attr in data:
                setattr(task, attr, data[attr])
            if "status" in data and data["status"] in STATUS:
                task.status = data["status"]
            db.session.commit()
            return task.to_dict(), 202
        except Exception as e:
            db.session.rollback()
            return {"message": "Something went wrong", "error": str(e)}, 400

    def delete(self, id):
        try:
            if not (task := Task.query.get(id)):
                return {"message": "Task not found"}, 404
            db.session.delete(task)
            db.session.commit()
            return {"message": "Task deleted"}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "Something went wrong", "error": str(e)}, 400


api.add_resource(Tasks, "/tasks")
api.add_resource(TaskById, "/tasks/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
