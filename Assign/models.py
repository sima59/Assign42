from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class barkyModel(db.Model):
    __tablename__ = "bookmarks"
 
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.text())
    url = db.Column(db.text())
    note = db.Column(db.text())
    date_added = db.Column(db.text())
 
    def __init__(self, id,title,url,note,date_added):
        self.id = id
        self.title = title
        self.url = url
        self.note = note
        self.date_added= date_added
 
    def __repr__(self):
        return f"{self.title}:{self.url}"
