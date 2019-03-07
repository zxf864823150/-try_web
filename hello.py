import flask as flask
import UserList as ul
import numpy as np
import pandas as pd
import tensorflow as tf
from flask_bootstrap import  Bootstrap
import FormClass
from flask import request
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename

__author__ = "zhaixiaofan"
__goal__ = "practice web app and make a class web "
__doc__ = "nothing to do "

#create app object
app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "has a hard pw"
bootstrap = Bootstrap(app)
new_user = ul.User_List()

"""see https://www.cnblogs.com/caodneg7/p/10139995.html"""
"""只能单页刷新，没有提示，需要使用session解决"""
@app.route("/",methods = ["POST","GET"])
def say_hello():
    form = FormClass.NameForm()
    name = None
    file = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        file = form.file.data
        print(file.filename.split("."))
        readname = file.filename.split(".")[0]
        pfilename = secure_filename(file.filename)
        filename = readname+"."+pfilename
        print(filename)
        file.save(filename)
    return flask.render_template("hello.html",form=form,name=name,file=file)

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

@app.route("/geturl",methods=["POST","GET","DELETE"])
def get_url():
    urlcon = flask.request.url
    print(urlcon)
    conn = flask.request.args.to_dict()
    print(conn)
    return str(conn)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)