#!/usr/bin/env python
# -- coding: utf-8 --
from dbConfig import *


@app.route('/schedule_student', methods=['POST'])
def schedule_student():
    try:
        data = request.json
        room_id = data["room_id"]

        # # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT * FROM schedule_student WHERE room_id = '""" + str(room_id) + """'"""
        # print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        # print(data_sql)
        # print(columns)
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