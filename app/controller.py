from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/play_game')
def play_game():
    return render_template('play_game.html')

@app.route('/game_result', methods=["POST"])
def game_result():
    form_data = request.form 
 
    player_1 = Player (form_data['player_1_name'], form_data['player_1_choice'])
    player_2 = Player (form_data['player_2_name'], form_data['player_2_choice'])
    r_p_s = Game("Rock Paper Scissors", player_1, player_2)
    r_p_s.play()
    return render_template('result.html', game = r_p_s)

@app.route('/<player_1_choice>/<player_2_choice>')
def test_game_result(player_1_choice,player_2_choice):
    player_1 = Player ("Boris the blade", player_1_choice)
    player_2 = Player ("Batman", player_2_choice)
    r_p_s = Game("Rock Paper Scissors", player_1, player_2)
    r_p_s.play()
    return render_template('result.html', game = r_p_s)