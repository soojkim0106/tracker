from sqlalchemy_serializer import SerializerMixin
from config import db

class Task(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Not Started")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }
        
    def __repr__(self):
        return f"<Task {self.id}: {self.title | self.description | self.status}>"