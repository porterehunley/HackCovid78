from app import db
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    user = db.Column(db.ForeignKey('user.username'))
    email = db.Column(db.String(120), index=True)
    rating = db.Column(db.Integer)
    body = db.Column(db.String(200))


    def __repr__(self):
        return str([self.username, self.body, self.email])

    def to_dict(self):
    	return { "id" : self.id, "username" : self.user, "title" : self.title, "email" : self.email, "rating" : self.rating, "body" : self.body }

   
   
