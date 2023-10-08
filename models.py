from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Entry(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    
    def __repr__(self):
        return f'<Content {self.content}>'

