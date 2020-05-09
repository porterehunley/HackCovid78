from app import db
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.Integer)
    body = db.Column(db.String(200))


    def __repr__(self):
        return str([self.username, self.body, self.email])