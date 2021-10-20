#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/homework', methods=['POST'])
def homework():
    try:
        data = request.json
        room = data["room"]

        # # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT cause_name, room,detail, date, file FROM `homework` WHERE room = '""" + str(room) + """'"""
        # ด้านหลังเช็คเป็น string เราสามารถใส่ """''""" เเบบนี้มันจะบอกเป็น string
        print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        print(data_sql)
        print(columns)
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