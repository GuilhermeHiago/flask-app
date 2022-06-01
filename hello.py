from flask import Flask, render_template, request, redirect, session, flash, url_for

class Game:
    def __init__(self, title, category) -> None:
        self.title = title
        self.category = category

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
    if session['current_user'] == 'admin':
        return render_template('gameregisterform.html', title="New Game")

    flash('Authentication Required')
    return redirect(url_for('login', next=url_for('game_register')))

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
    if "1234" == request.form['password']:
        session['current_user'] = request.form['user']
        flash(session['current_user'] + ' loged in')

        next_page = request.form['next']
        print(next_page)
        return redirect(next_page)
    else:
        flash('Login Failed')
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session['current_user'] = None
    flash('Logout Successful')

    return redirect(url_for("index"))

app.run(debug=True)