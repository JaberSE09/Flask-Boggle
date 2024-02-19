from flask import Flask, request, render_template, jsonify, session

from boggle import Boggle


boggle_game = Boggle()

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
app.config["SECRET_KEY"] = "jfkjdslkjfdssjfdd"

@app.route('/')
def home():
    board = boggle_game.make_board()
    session["board"] = board
    highScore = session.get("highScore" , 0)
    plays = session.get("plays" , 0)
    return render_template("home.html" , board=board, highScore=highScore,plays=plays )
@app.route('/check-word')
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():

    score = request.json["score"]
    highScore = session.get("highScore", 0)
    plays = session.get("plays", 0)

    session['plays'] = plays + 1
    session['highScore'] = max(score, highScore)

    return jsonify(brokeRecord=score > highScore)
