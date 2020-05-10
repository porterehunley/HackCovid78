from app import db
class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.ForeignKey('user.id'))
    post = db.Column(db.ForeignKey('post.id'))
    email = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.Integer)
    body = db.Column(db.String(200))


    def __repr__(self):
        return str([self.username, self.body, self.email])

    def to_dict(self):
    	return {
    		"id" : self.id,
    		"username" : self.username,
    		"post" : self.post,
    		"email" : self.email,
    		"rating" : self.rating,
    		"body" : self.body
    	}