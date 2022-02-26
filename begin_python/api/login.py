#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *

#ไว้ confiq
@app.route('/login', methods=['POST']) 
def login():
    try:
        data = request.json
        username = data["username"]
        password = data["password"]

        # connect db
        conn = connectToDB() #ไว้เชื่อมดาต้าเบส #เอาไว้เปิด
        cursor = conn.cursor() #ทำงานอยู่ที่ไหน

        # sql = """ SELECT id,role_id FROM account WHERE username = %s AND password = %s"""
        sql = """ SELECT account.id,account.role_id,profile.id AS std_id FROM account INNER JOIN profile ON account.id = profile.account_id WHERE username = %s AND password = %s """
        print(sql)
        cursor.execute(sql,(username,password))
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description] #เอาstring มาต่อกันฃ
        print (columns)
        print (data_sql)
        result = toJson(data_sql,columns)
        if len(result) > 0:
            result = {"status":"OK","result":result}
        else:
            result = {"status":"ER","errorMessage":"Username or Password in correct"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally: #ทุก api ต้องreturn ออก
        conn.close()
        return result