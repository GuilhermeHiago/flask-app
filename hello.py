from flask import Flask, render_template, request, redirect, session, flash, url_for
import MySQLdb
import sys

class Game:
    def __init__(self, title, category) -> None:
        self.title = title
        self.category = category

class User():
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password

user1 = User('user1', '1111')
user2 = User('user2', '2222')

users = {user1.name:user1, user2.name: user2}

game1 = Game('God of War', 'Hank and Slash')
game2 = Game('Valorant', 'FPS')
game3 = Game('GTA V', 'Action')
game_list = [game1, game2, game3]

app = Flask(__name__)
app.secret_key = "flaskapp"

@app.route("/")
def index():
    return render_template('list.html', title="Games", items=game_list)

@app.route('/gameregister')
def game_register():
    if 'current_user' not in session or session['current_user'] == None:
        flash('Authentication Required')
        return redirect(url_for('login', next=url_for('game_register')))

    return render_template('gameregisterform.html', title="New Game")

@app.route('/gamecreate', methods=['POST',])
def game_create():

    # for i in request.form:
    #     print(request.form[0])
    title = request.form['game-title']
    category = request.form['category']
    console = request.form['console']

    game = Game(title, category)
    game_list.append(game)
    
    #return render_template('list.html', title="Games", items=game_list)
    return redirect(url_for("index"))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/authenticate', methods=['POST',])
def authenticate():
    
    if request.form['user'] in users:
        user = users[request.form['user']]

        if request.form['password'] == user.password:
            session['current_user'] = user.name
            flash(user.name + ' loged in')

            next_page = request.form['next']

            return redirect(next_page)

    flash('Login Failed')
    return redirect(url_for("login"))
    

@app.route('/logout')
def logout():
    session['current_user'] = None
    flash('Logout Successful')

    return redirect(url_for("index"))

app.run(debug=True)