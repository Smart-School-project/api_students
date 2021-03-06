#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/submitleave', methods=['POST'])
def submitleave():
    try:
        data = request.json
        account_id = data["account_id"]



        # # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT * FROM `leave` WHERE account_id = '""" + str(account_id) + """' """ 
        # ด้านหลังเช็คเป็น string เราสามารถใส่ """''""" เเบบนี้มันจะบอกเป็น string
        print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = toJson(data_sql,columns)
        print(data_sql)
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