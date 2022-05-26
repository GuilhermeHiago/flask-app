from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    game_list = ['God of War', 'Valorant', 'GTA V']
    return render_template('list.html', title="Games", items=game_list)