from dbConfig import *

@app.route('/leave', methods=['POST'])
def leave():
    try:
        data = request.json
        # id = data["id"]
        date = data["date"]
        account_id = data["account_id"]
        name = data["name"]
        students_id = data["students_id"]
        room = data["room"]
        type_leave = data["type_leave"]
        subject = data["subject"]
        teacher = data["teacher"]
        cause = data["cause"]
        pdf = data["pdf"]

        # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ INSERT INTO `leave` (account_id ,date, name, students_id, room, type_leave, subject, teacher, cause, pdf) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s) """   
        cursor.execute(sql,(account_id,date,name,students_id,room,type_leave,subject,teacher,cause,pdf))
        conn.commit()

        # data_sql = cursor.fetchall()
        # columns = [column[0] for column in cursor.description]
        # result = toJson(data_sql,columns)

        result = {"status":"OK","result":"เพิ่มข้อมูลสำเร็จ"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        conn.close()
        return result