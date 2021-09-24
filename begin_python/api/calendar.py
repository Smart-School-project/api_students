#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/calendar', methods=['POST'])
def calendar():
    try:
        data = request.json
        name = data["name"]

        # # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT name , start , details , end FROM calendar WHERE name = '""" + str(name) +  """'"""
        print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = toJson(data_sql,columns)
        if len(result) > 0:
            result = {"status":"OK","result":result}
        else:
            result = {"status":"ER","errorMessage":"ไม่พบ ข้อมูล"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        # conn.close()
        return result
