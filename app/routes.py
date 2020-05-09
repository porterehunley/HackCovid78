import json

from app import app
from app import db 
from app.models import User

from flask import Response
from flask import jsonify
from flask import request

import requests 

class Gender:
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"

# class User:
#     def __init__(self, username, password, zip_code, tested, infected, high_risk, gender, age, rating):
#         self.username = username
#         self.password = password
#         self.zip_code = zip_code
#         self.tested = tested
#         self.infected = infected
#         self.high_risk = high_risk
#         self.gender = gender
#         self.age = age
#         self.rating = rating
    
#     def __repr__(self):
#         return str([self.username, self.zip_code, self.tested, self.infected])
    
# class UserDB:
#     def __init__(self):
#         self.db = {}
    
#     def __str__(self):
#         return str(self.db)
    
#     def addUser(self, user):
#         self.db[user.username] = user
    
#     def isInfected(self, username):
#         return username in self.db and self.db[username].infected

# userDB = UserDB()

@app.route('/adduser/', methods=['POST'])
def addUser():
    data = request.get_json() or {}
    u = User(username=data['username'], email=data['email'], password_hash=data['password'], zip_code=data['zip_code'], 
        tested=data['tested'], infected=data['infected'], high_risk=data['high_risk'])
    db.session.add(u)

    return Response("{'status':'user added'}", status=200, mimetype='application/json')

@app.route('/getuser/<username>', methods=['GET'])
def getUser(username):
    user = User.query.filter_by(username=username).first()
    print(user)
    return Response(json.dumps(user), status=200, mimetype='application/json')


@app.route('/viewUsers')
def viewUsers():
    return str(userDB)
