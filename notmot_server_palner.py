import mysql.connector as mysql
import datetime




def date_and_time():
    cu = datetime.datetime.now()
    time = cu.strftime('%H:%M %p')
    date = datetime.date.today()
    
    return [time , date]


#--------------------main connection------------------------------------
database = mysql.connect(host = "localhost" , user = "root" , passwd = "admin", database = "notmotinfo")
cursor = database.cursor()

#-----------------------------------------------------------------------

def counter(): #id counter
    try :
        query = ("SELECT * FROM planinfo WHERE counterpointer = 2024")
        cursor.execute(query)
        for i in cursor :
            (source) = i[6]
        
        query = ("UPDATE planinfo SET counter = %s WHERE counterpointer = %s")
        
        values = (str(int(source) + 1) , "2024")
        cursor.execute(query , values)
        database.commit()
        
        return source
    except Exception as e :
        print(e)
        return False


def add_to_db(note) :
    try :
        time = date_and_time()[0]
        date = date_and_time()[1]
        query = ("INSERT INTO planinfo(id , plan , time , date , status ,counter , counterpointer) VALUES(%s , %s , %s , %s , 0 , 0 , 0)") #table name <---------------
        id = counter()
        values = (id , note , str(time) , str(date))
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e:
        print(e)
        return False


def del_from_db(id) :
    try :
        query = ("DELETE FROM planinfo WHERE id = %s and id = %s") #table name <---------------
        values = (id , id) #im copy that bc sql have bug 
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e :
        print(e)
        return False


def switch_status_on_db(id , status):
    try :
        query = ("UPDATE planinfo SET status = %s WHERE id = %s") #table name <--------------
        values = (status , id)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e :
        print(e)
        return False
    
    
def show_data_from_db(date):
    try :
        query = (f"SELECT date = {date} FROM planinfo") #table name <--------------
        cursor.execute(query)
        data = []
        for i in cursor :
            data.append(i)
        return data
    except Exception as e :
        print(e)
        return False
