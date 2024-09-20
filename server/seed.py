from app import app
from config import db
from models.goal import Goal

with app.app_context():
    Goal.query.delete()
    print("Deleted all goals")
    
    goal1 = Goal(title="Finish backend", description= "Tracker backend must finish by EOD", status="In Progress")
    
    db.session.add(goal1)
    db.session.commit()
    
    print("Added a goal")