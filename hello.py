import string
from turtle import title
from flask import Flask, render_template

class Game:
    def __init__(self, title:string, category) -> None:
        self.title = title
        self.category = category


app = Flask(__name__)

@app.route("/")
def hello_world():
    game1 = Game('God of War', 'Hank and Slash')
    game2 = Game('Valorant', 'FPS')
    game3 = Game('GTA V', 'Action')
    game_list = [game1, game2, game3]
    return render_template('list.html', title="Games", items=game_list)

@app.route('/gameregister')
def game_register_form():
    return render_template('gameregisterform.html', title="New Game")

@app.route('/gamecreate')
def game_create():
    pass