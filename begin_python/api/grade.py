#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *
from ast import literal_eval
@app.route('/grade', methods=['POST'])
def grade():
    try:
        data = request.json
        # course_id = data["course_id"]
        # room = data["room"]
        id_std = data["id_std"]
        result = []

        # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = " SELECT * FROM `score` WHERE id_std = " + str(id_std)
        
        # print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        print(data_sql)
        columns = [column[0] for column in cursor.description]
        result = toJson(data_sql,columns)
        if len(result) >= 0:
            item_score = []
            for i in result:
                i['indicators'] = literal_eval(i['indicators'])
                i['itemScore'] = literal_eval(i['itemScore'])
                if i['itemScore'] not in item_score:
                    item_score.append(i['itemScore'])
            result = {"status":"OK","result":result, "item_score": item_score}
        else:
            result = {"status":"ER","errorMessage":"Not found"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        conn.close()
        return result