from app import app
class Gender:
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"

class User:
    def __init__(self, username, password, zip_code, tested, infected, high_risk, gender, age, rating):
        self.username = username
        self.password = password
        self.zip_code = zip_code
        self.tested = tested
        self.infected = infected
        self.high_risk = high_risk
        self.gender = gender
        self.age = age
        self.rating = rating
    
    def __repr__(self):
        return str([self.username, self.zip_code, self.tested, self.infected])
    
class UserDB:
    def __init__(self):
        self.db = {}
    
    def __str__(self):
        return str(self.db)
    
    def addUser(self, user):
        self.db[user.username] = user
    
    def isInfected(self, username):
        return username in self.db and self.db[username].infected

userDB = UserDB()

@app.route('/addUser/<username>')
def addUser(username):
    userDB.addUser(User(username, "juuuuu", 30332, True, False, False, Gender.FEMALE, 19, 3))
    return 200

@app.route('/viewUsers')
def viewUsers():
    return str(userDB)

if __name__ == '__main__':
    app.run()