#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re
import numpy as np
import time
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import requests
import os
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "autofill"
app.config["MONGO_URI"] = "mongodb://ppp:PANKIL@cluster0-shard-00-00-tqm1v.mongodb.net:27017,cluster0-shard-00-01-tqm1v.mongodb.net:27017,cluster0-shard-00-02-tqm1v.mongodb.net:27017/autofill?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
mongo = PyMongo(app)

atts = []####

data_values = {}
html_data = []
def func(link):
    atts.clear()
    html_data.clear()
    content = requests.get(link)
    soup = BeautifulSoup(content.text, 'html.parser')
    for t in soup.select('input'):
        html_dict = {}
        #x = str(t).split(" ")###
        #print(x)
        if(('type="text"' in str(t) or 'type="password"' in str(t) or 'type="email"' in str(t) ) and 'hidden="hidden"' not in str(t)):
            #print(str(t))
            #FIND IDS
            num = str(t).find("id=")
            itr = num+4
            id_string = ""
            while(str(t)[itr] != '"'):
                id_string += str(t)[itr]
                itr+=1
            html_dict['id'] = id_string
            
            #FIND NAMES
            num = str(t).find("name=")
            itr = num+6
            id_string = ""
            while(str(t)[itr] != '"'):
                id_string += str(t)[itr]
                itr+=1
            html_dict['name'] = id_string
            html_dict['dname'] = re.sub('[^A-Za-z0-9]+', '', id_string.lower())

            #FIND AREA LABEL
            num = str(t).find("area-label=")
            itr = num+20
            id_string = ""
            while(str(t)[itr] != '"'):
                id_string += str(t)[itr]
                itr+=1
            html_dict['area-label'] = re.sub('[^A-Za-z0-9]+', '', id_string.lower())
            html_data.append(html_dict)


    #print(existing_user['first_name'])
    #DATA OF USER
    users = mongo.db.users
    existing_user = users.find_one({'email' : session['email']})
    for i in existing_user:
        #print(i)
        if(i in "_id"):
            continue
        atts.append(re.sub('[^A-Za-z0-9]+', '', str(i).lower()).replace(" ",""))
    #print(atts)
    counter=0
    #print(existing_user)
    for i in existing_user:
        #print(i)
        if(i == "_id" or i == " id" or i ==  "id"):
            continue
        data_values[atts[counter]] = existing_user[str(i)]
        counter+=1
    reponse = []
    reponse.append(html_data)
    reponse.append(atts)
    print(html_data)
    print(atts)
    return reponse
def autoupdate_texti():
    users = mongo.db.users
    existing_user = users.find_one({'email' : session['email']})
    #print(html_data)
    for i in html_data:
        flag=0
        try:
            val =browser.find_element_by_id(i['id']).get_attribute('value')

            for j in existing_user:
                if('password' in str(j)):
                    continue
                if(str(j) in i['dname']):
                    flag=1
                    break
            if(flag==0):
               # print(val)
                #existing_user.insert({i['name'] : val})
                if('password' in i['dname']):
                    link = browser.current_url
                   # print(str(link).split('.')[0])
                    users.update({"email": existing_user["email"]}, {"$set": {str(link).split('.')[0]: val}})
                else:       
                    users.update({"email": existing_user["email"]}, {"$set": {i['name'] : val}})
                atts.append(i['name'])
               # print("Successful")
        except:
            time.sleep(1)
    #print(html_data)
    return 'OK'
