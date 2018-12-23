import flask as flask
import UserList as ul
import numpy as np
import pandas as pd


__author__ = "zhaixiaofan"
__goal__ = "practice web app and make a class web "
__doc__ = "nothing to do "

#create app object
app = flask.Flask(__name__)

new_user = ul.User_List()

@app.route("/",methods = ["POST","GET"])
def say_hello():
    return flask.render_template("sigin.html",name="welcome")
#'''
@app.route("/login",methods = ["POST","GET"])
def login():
    return flask.render_template("login_new.html")

@app.route("/home_page",methods = ["POST","GET"])
def home_page():
    if flask.request.method == "POST":
        return flask.render_template("cainiao.html")#flask.render_template使用模板
    #else:
     #   return flask.redirect(say_hello)
#'''
@app.route("/save_user",methods = ["POST","GET"])
def save_user():
    global new_user
    if flask.request.method == "POST":
        use_name = flask.request.form["alias"]
        print(use_name)
        use_password = flask.request.form["password"]
        print(use_password)
        if  len(use_name) != 0\
                and len(use_password) != 0:
            new_user._add_user(use_name,use_password)
            return flask.render_template("sigin.html")
        else:
            return flask.render_template("login_new.html")
    #else:
        #return flask.render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)