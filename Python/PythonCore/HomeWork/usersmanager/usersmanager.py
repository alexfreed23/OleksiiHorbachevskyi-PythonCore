#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:40:24 2020

@author: oleksii
"""

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template


app = Flask(__name__)

listOfUsers = ["vasyapupkin", "limberkaufman", "arisumialbertsen", "giovaninifroyd", "clasespratlin", "merrickzarlenga", "chhordorweiler", "argetsingerbandura", "schrackzemlicka","smecknisbit"]

userdetailsInfo = {"vasyapupkin":{"firstname": "Vasya", "lastname": "Pupkin", "age": 33, "username": "vasyapupkin"},
                   "limberkaufman":{"firstname": "Limber", "lastname": "Kaufman", "age": 34, "username": "limberkaufman"},
                   "arisumialbertsen":{"firstname": "Arisumi", "lastname": "Albertsen", "age": 44, "username": "arisumialbertsen"},
                   "giovaninifroyd":{"firstname": "Giovanini", "lastname": "Spratlin", "age": 63, "username": "giovaninifroyd"},
                   "clasespratlin":{"firstname": "Clase", "lastname": "Pupkin", "age": 23, "username": "clasespratlin"},
                   "merrickzarlenga":{"firstname": "Merrick", "lastname": "Zarlenga", "age": 29, "username": "merrickzarlenga"},
                   "chhordorweiler":{"firstname": "Chhor", "lastname": "Dorweiler", "age": 19, "username": "chhordorweiler"},
                   "argetsingerbandura":{"firstname": "Argetsinger", "lastname": "Bandura", "age": 22, "username": "argetsingerbandura"},
                   "schrackzemlicka":{"firstname": "Schrack", "lastname": "Zemlicka", "age": 77, "username": "schrackzemlicka"},
                   "smecknisbit":{"firstname": "Smeck", "lastname": "Nisbit", "age": 3, "username": "smecknisbit"}}
groupslist = []


@app.route('/')
@app.route('/home')
def home(name=None):
    return render_template('index.html')

@app.route('/userslist')
def userslist():
    return render_template('/userslist.html', listOfUsers=listOfUsers)


@app.route('/userslist/<username>')
def userdetails(username):
    return render_template('/userslistuserdetails.html', user = username,
                           firstname = userdetailsInfo[username]["firstname"], 
                           lastname = userdetailsInfo[username]["lastname"], 
                           age = userdetailsInfo[username]["age"], 
                           username = userdetailsInfo[username]["username"])


@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        listOfUsers.append(username)
        userdetailsInfo.update({username:{"firstname":firstname, "lastname":lastname, "age":age, "username":username}})
    return render_template('/adduser.html')


@app.route('/addgroup',methods=['POST', 'GET'])
def addgroup():
    if request.method == 'POST':
        groupname = request.form['groupname']
        groupslist.append(groupname)
    return render_template('/addgroup.html', groupslist=groupslist)


@app.route('/about')
def about():
    return render_template('/about.html')

if __name__=='__main__':
    app.run(debug = True)

