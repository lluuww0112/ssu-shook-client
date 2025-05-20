from flask import Flask, jsonify, request
from flask import render_template, url_for
from flask import app
import requests


from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def Login_Page():
    return render_template('/login/login.html')

@app.route("/regist")
def Regist_Page():
    return render_template('/regist/regist.html')

@app.route("/home")
def Main_Page():
    return render_template("/home/home.html")


@app.route("/clubs")
def Recommand_page():
    return render_template("/home/clubs.html")

@app.route("/ranking")
def Ranking_Page():
    return render_template("/home/ranking.html")

@app.route("/activity")
def Activity_Page():
    return render_template("/home/activity.html")

@app.route("/recruiting")
def Recruiting_Page():
    return render_template("./home/recruiting.html")


@app.route("/NewClub")
def NewClub_Page():
    return render_template("./home/NewClub.html")


@app.route("/clubs/club")
def Club_Page():
    return render_template("./club/club.html")


@app.route("/clubs/club/activity")
def Club_activity():
    return render_template("./club/activity.html")


@app.route("/clubs/club/management")
def Club_management():
    return render_template("./club/management.html")

@app.route("/user/get_posts")
def User_get_posts():
    return render_template("./user/get_posts.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3001, debug=True)
