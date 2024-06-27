
def switch_status_on_db(id , status):
    try :
        query = ("UPDATE notinfo SET status = %s WHERE id = %s") #table name <--------------
        values = (status , id)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e :
        print(e)
        return False
    