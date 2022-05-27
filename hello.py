from flask import Flask, render_template, request

class Game:
    def __init__(self, title, category) -> None:
        self.title = title
        self.category = category

game1 = Game('God of War', 'Hank and Slash')
game2 = Game('Valorant', 'FPS')
game3 = Game('GTA V', 'Action')
game_list = [game1, game2, game3]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('list.html', title="Games", items=game_list)

@app.route('/gameregister')
def game_register_form():
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
    
    return render_template('list.html', title="Games", items=game_list)

app.run(debug=True)