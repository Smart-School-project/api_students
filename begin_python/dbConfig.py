#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify, current_app,send_from_directory,send_file,abort,redirect,session,render_template,make_response
from flask_cors import CORS, cross_origin
import io

import mysql.connector
from mysql.connector import (connection)

app = Flask(__name__)
CORS(app)

def connectToDB():
    try:
        #connectionString = mysql.connector.connect(host='localhost',database='project',user='root',password='',port=3306)
        connectionString = mysql.connector.connect(host='sql6.freesqldatabase.com',database='sql6475527',user='sql6475527',password='BrdmWhME71',port=3306)
        print(connectionString)
    except Exception as e:
        print(e)
    try:
        return connectionString
    except:
        return jsonify({'status':'fail','message':'Something went wrong'})


def toJson(data,columns):
    results = []
    for row in data:
        results.append(dict(zip(columns, row)))
    return results
