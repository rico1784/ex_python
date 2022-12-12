import mysql.connector as connector

class processUser:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_ok = False

    def insertUser(email,password):
        db= connector.connect(
            user='root',
            password='',
            host='localhost',
            database='users'
        )
        ma_bdd = db.cursor()
        data = (email, password)
        request = "INSERT INTO user (email, password) VALUES (%s, %s)"
        ma_bdd.execute(request, data)
        ma_bdd.close()
        db.commit()
        db.close()
        return True

    def checkUser(email):
        db= connector.connect(
            user='root',
            password='',
            host='localhost',
            database='users')
        ma_bdd = db.cursor()
        data = (email[0])
        request = '''(SELECT * FROM user WHERE email='%s')'''%data
        ma_bdd.execute(request)
        user = ma_bdd.fetchall()
        ma_bdd.close()
        return user
