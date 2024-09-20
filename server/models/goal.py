from sqlalchemy_serializer import SerializerMixin
from config import db

class Goal(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Not Started")
    
    def __repr__(self):
        return f"<Goal {self.id}: {self.title | self.description | self.status}>"