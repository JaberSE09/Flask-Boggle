from flask import Flask, request, render_template, jsonify, session

from boggle import Boggle


boggle_game = Boggle()

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
app.config["SECRET_KEY"] = "jfkjdslkjfds;lsjfdd"

@app.route('/')
def home():
    board = boggle_game.make_board()
    session["board"] = board
    highScore = session.get("highScore" , 0)
    plays = session.get("plays" , 0)
    return render_template("home.html" , board=board, highScore=highScore,plays=plays )