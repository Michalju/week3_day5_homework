from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player



@app.route('/<player_1_choice>/<player_2_choice>')
def index(player_1_choice,player_2_choice):
    player_1 = Player ("Boris the blade", player_1_choice)
    player_2 = Player ("Batman", player_2_choice)
    r_p_s = Game("Rock Paper Scissors", player_1, player_2)
    r_p_s.play()
    return render_template('result.html', game = r_p_s)