from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    zip_code = db.Column(db.String(64))
    tested = db.Column(db.Boolean)
    infected = db.Column(db.Boolean)
    high_risk = db.Column(db.Boolean)
    # self.gender = db
    # self.age = age
    # self.rating = rating

    def __repr__(self):
        return str([self.username, self.zip_code, self.tested, self.infected])