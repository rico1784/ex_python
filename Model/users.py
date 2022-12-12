import mysql.connector as connector

class processUser:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_ok = False

    def insertUser(self):
        db= connector.connect(
            user='root',
            password='',
            host='localhost',
            database='users'
        )
        ma_bdd = db.cursor()
        ma_bdd.execute("INSERT INTO user (email, password) VALUES (?, ?)")
        ma_bdd.execute(self.email, self.password)
        ma_bdd.close()
        db.commit()
        db.close()
        return True

    def checkUser(self):
        db= connector.connect(
            user='root',
            password='',
            host='localhost',
            database='user')
        ma_bdd = db.cursor()
        ma_bdd.execute('SELECT email, password FROM users WHERE email=?', self.email)
        user = ma_bdd.fetchall()
        ma_bdd.close()
        return user
