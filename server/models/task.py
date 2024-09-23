from sqlalchemy_serializer import SerializerMixin
from config import db


class Task(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Not Started")

    def validate_title(self, title):
        if not title or len(title.strip()) == 0 or len(title) > 20:
            raise ValueError(
                "Title must be between 1 and 20 characters long and cannot be empty or whitespace"
            )

    def validate_description(self, description):
        if not description or len(description.strip()) == 0 or len(description) > 100:
            raise ValueError(
                "Description must be between 1 and 100 characters long and cannot be empty or whitespace"
            )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }

    def __repr__(self):
        return f"<Task {self.id}: {self.title | self.description | self.status}>"
