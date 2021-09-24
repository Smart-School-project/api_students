#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/calendar', methods=['POST'])
def calendar():
    try:
        data = request.json
        start = data["start"]
        end = data["end"]

        # # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT name , start , end FROM `calendar` WHERE `start` BETWEEN '""" + str(start) + """' AND '""" + str(end) + """'"""
        # print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        # print(columns)
        # print(data_sql)
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
