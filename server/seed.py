from app import app
from config import db
from models.task import Task

with app.app_context():
    Task.query.delete()
    print("Deleted all tasks")

    task1 = Task(
        title="Finish backend",
        description="Tracker backend must finish by EOD",
        status="Completed",
    )
    task2 = Task(
        title="Finish frontend",
        description="Tracker frontend must finish by EOD",
        status="In Progress",
    )
    task3 = Task(
        title="Finish testing",
        description="Tracker design must finish by EOD",
        status="Not Started",
    )

    tasks = [task1, task2, task3]

    db.session.add_all(tasks)
    db.session.commit()

    print("Added task")
