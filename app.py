from flask import Flask, render_template
from flask import request
from mysql import connector
import os
from Model import users

app = Flask(__name__)
# Gestion des images:
IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


# Définition des routes
@app.route('/')
def routeAccueil():
    entreeSite_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'entree.jpg')
    return render_template("index.html", user_image=entreeSite_Logo)



@app.route('/login', methods=['POST', 'GET'])
def routeLogin():
    db = connector.connect(
        user = 'root',
        password = '',
        database = 'users',
        host = 'localhost'
    )
    ma_bdd = db.cursor()
    if request.method == 'POST':

        query=("SELECT * from user WHERE email = %s")
        postemail = request.form['postEmail']
        password = request.form['postPassword']
        ma_bdd.execute(query, postemail)
        user = ma_bdd.fetchall()
        message = user
        return render_template('login.html', message=message)


    return render_template('login.html')


    #
    # addr_mail = "example@example.fr"
    # addr_pass = "example"
    # if request.method == "POST":
    #     message = ''
    #     post_mail = request.form['postEmail']
    #     post_pass = request.form['postPassword']
    #     if addr_mail == post_mail and addr_pass == post_pass:
    #         message = 'Connexion réussie.'
    #
    #     elif addr_mail == post_mail:
    #         message = 'Mot de passe incorrect'
    #     else:
    #         message = 'user et password faux'
    #     return render_template('login.html', message=message)
    #
    #
    #
    #




@app.route('/signup', methods=['POST', 'GET'])
def routeSignup():
    if request.method == "POST":
        message = ''
        addEmail = request.form['addEmail']
        password = request.form['addPassword']
        addCheckPassword = request.form['addCheckPassword']

        if password == addCheckPassword:
            add_user = users.processUser.insertUser(addEmail, password)
            if add_user:
                message = 'Votre compte a été créer'
                return render_template('signup.html', message=message)
            else:
                message = 'Les mots de passe me correspondent pas'
                return render_template('signup.html', message=message)


    return render_template('signup.html')

