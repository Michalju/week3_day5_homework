from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player



@app.route('/<var1>/<var2>')
def index(var1,var2):
    player_1 = Player ("Boris the blade", var1)
    player_2 = Player ("Batman", var2)
    rock_paper_scissors = Game("Rock Paper Scissors", player_1, player_2)

    return render_template('index.html', title = rock_paper_scissors.play())

