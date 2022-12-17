from flask import Flask, render_template, redirect
from flask import request
import os
from Model import database



app = Flask(__name__)
# Gestion des images:
IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

# Déclaration de la liste de l'utilisateur connecté
user_connected = []

######### Définition des routes#########
# Route de la page principale
@app.route('/')
def routeAccueil():
    entreeSite_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'entree.jpg')
    if user_connected:
        user = str(user_connected[0])
        isConnected = bool(user_connected[1])
        return render_template('index.html',
                                isConnected=isConnected,
                                user_image=entreeSite_Logo,
                                message=user_connected,
                                user=user,
                                Title='Exercice Python - Accueil'
                               )
    else:
        user = 'utilisateur anonyme'
        return render_template('index.html',
                               user_image=entreeSite_Logo,
                               message=user_connected,
                               user=user,
                               Title='Exercice Python - Accueil'
                               )
    return render_template('index.html', Title='Exercice Python - Accueil')

# Route de la page login
@app.route('/login', methods=['POST', 'GET'])
def routeLogin():
    if request.method == 'POST':
        postemail = request.form['postEmail']
        password = request.form['postPassword']

        if not postemail:
            return render_template('login.html', message='Veuillez compléter le formulaire')
        elif not password and postemail:
            return render_template('login.html', message='Il manque le mot de passe')
        else:
            try:
                manager = database.DatabaseManager()
                manager.execute_query('SELECT * FROM users.user WHERE email = %s', (postemail,))
                results = manager.fetch_all()
                manager.close_connection()
                passuser = results[0][2]

                if passuser == password:
                    user_connected.extend([postemail, True])
                    return render_template('login.html',
                                            message='Connexion OK',
                                            Title = 'Exercice Python - Login',
                                            isConnected=bool(user_connected[1])
                                       )
                elif passuser != password:
                    return render_template('login.html',
                                           message='Connexion échouée',
                                           Title = 'Exercice Python - Login'
                                           )
            except:
                return render_template('login.html',
                                       message='Connexion échouée',
                                       Title='Exercice Python - Login'
                                       )
    return render_template('login.html',
                           Title='Exercice Python - Login'
                           )


# Route de la page signup
@app.route('/signup', methods=['POST', 'GET'])
def routeSignup():
    if request.method == "POST":
        message = ''
        addEmail = request.form['addEmail']
        password = request.form['addPassword']
        addCheckPassword = request.form['addCheckPassword']
        try:
            if password == addCheckPassword:
                manager = database.DatabaseManager()
                manager.execute_query('INSERT INTO users.user (email, password) VALUES (%s, %s)', (addEmail, password))
                return render_template('signup.html',
                                    message='Votre compte a été créer',
                                    Title = 'Exercice Python - Signup',
                                    loginOK = True
                                   )
            elif password != addCheckPassword:
                message = 'Les mots de passe me correspondent pas'
                return render_template('signup.html',
                                   message=message,
                                   Title = 'Exercice Python - Signup')
        except:
            return render_template('signup.html',
                                   message='Sauvegarde impossible',
                                   Title = 'Exercice Python - Signup'
                                   )

    return render_template('signup.html',
                           Title = 'Exercice Python - Signup'
                           )

@app.route('/logout')
def routeLogout():
    user_connected.clear()
    return redirect('/')



app.debug = True
app.run