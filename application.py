#!/usr/bin/env python3
from flask import Flask, render_template, url_for, request, session, redirect,Markup, flash
from flask_pymongo import PyMongo
import autofill
import os
import sys
from functools import wraps
import time
from flask import jsonify

#print (os.environ)
#from passlib.hash import sha256_crypt
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "autofill"
app.config["MONGO_URI"] = "mongodb://ppp:PANKIL@cluster0-shard-00-00-tqm1v.mongodb.net:27017,cluster0-shard-00-01-tqm1v.mongodb.net:27017,cluster0-shard-00-02-tqm1v.mongodb.net:27017/autofill?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    email = request.args.get('email', None)
    password = request.args.get('password', None)
    if request.method == 'POST' or request.method == 'GET': 
        users = mongo.db.users
        login_use = users.find_one({'email' : email})
       # print(login_user)
        if login_use:
            if (password == login_use['password']):
                session['email'] = email
                session['name'] = login_use['firstname']
                session['times'] = login_use['times']
                login_user = []
                for i in login_use:
                    if(i in "_id"):
                        continue
                    login_user.append({str(i) : login_use[str(i)]})
                print(login_user)
                return jsonify(login_user)
            else :
                message = Markup("<strong> Password is wrong </strong>")
                flash(message)
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email' : request.form['email']})

        if existing_user is None:
            hashpass=(request.form['pwd'])
            #print(sha256_crypt.verify("password", password))
            users.insert({'firstname' : request.form['first_name'],'lastname' : request.form['last_name'] ,'email' : request.form['email'], 'password' : hashpass,
            'address1' : request.form['address1'],'address2' : request.form['address2'],
            'zipcode' : request.form['zipcode'],'city' : request.form['city'],
            'state' : request.form['state'],'phoneno' : request.form['phone_no'],'username' : request.form['username'],
            'times' : '1'
            })
            session['email'] = request.form['email']
            session['name'] = request.form['first_name']
            session['times'] = '1'
            return render_template("login.html")
        
        return 'That Account already exists!'

    return render_template('signup.html')

@app.route('/autofill', methods=['POST', 'GET'])
def autofill_text():
    users = mongo.db.users
    url = request.args.get('url', None)
    print(url)
    #existing_user = users.find_one({'email' : session['email']})

    if(request.method == 'POST'):
       # print(str(int(existing_user['times'])+1))
        users.update({'email': existing_user['email']}, {'$set' : {'times' : str(int(existing_user['times'])+1)}})
        existing_user = users.find_one({'email' : session['email']})
        session['times'] = existing_user['times']
        #print('after' +  session['times'])
        return render_template("autoupdate.html")
    else:
        return jsonify(autofill.func(url))
         
@app.route('/autoupdate', methods=['POST', 'GET'])
def autoupdate_text():
    idd = request.args.get('id', None)
    val = request.args.get('value', None)

    if(request.method == 'POST'):
        message = Markup("<strong> Autoupdate is successful , go to details to watch new details.</strong>")
        flash(message)
        print("gggggg")
        return autofill.autoupdate_texti(idd,val)
    else:
        return autofill.autoupdate_texti(idd,val)

@app.route('/details', methods=['POST', 'GET'])
def details():
    rows = {}
    users = mongo.db.users
    existing_user = users.find_one({'email' : session['email']})
    if(request.method == 'GET'):
        for i in existing_user:
            rows[str(i)] = str(existing_user[str(i)]) 
        #print(rows)
        return render_template("details.html",rows=rows)

    elif(request.method == 'POST'):
        #print(existing_user['email'])
        for j in existing_user:
            if(j not in "_id" and j not in "password" and j not in "times"):
                rows[str(j)] = str(existing_user[str(j)]) 
                #print(request.form['first_name'])
                users.update({'email': existing_user['email']}, {'$set' : {str(j) : request.form[str(j)]}})
        #print(rows)
        message = Markup("<strong> Details Successfully updated.</strong>")
        flash(message)
        return redirect(url_for('details'))
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/help')
def help():
    return render_template('help.html')
@app.route('/after_login')
def after_login():
	return render_template('after_login.html')

app.secret_key = 'mysecret'

if __name__ == '__main__':  
    app.run(debug=True)
