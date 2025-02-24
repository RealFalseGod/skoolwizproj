from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

class to_do_list(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    task=db.Column(db.String(400),nullable=False)
    date_to_do=db.Column(db.Date,default=datetime.utcnow().date,nullable=False)
    done=db.Column(db.Boolean,default=False)
    def __repr__(self):
        return (f"<to_do_list(id={self.id},title='{self.title} ,task='{self.task}',date={self.date} ,done={self.done})>")
    