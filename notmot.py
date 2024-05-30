import mysql.connector as mysql
from colorama import Fore
import socket
import argparse
import requests
import datetime 
import os


#Enter database information
"""
datebase name = notmotinfo
table name = notinfo
"""
#---------------------------


"""
description :

"""


def clear_screen(): #you can use clear screen on windows/linux/mac
    if os.name == "nt" :
        os.system("cls")
    else :
        os.system("clear")
        
        
def check_internet_connection(): #check internet connection with google domain
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
    

def check_server_connection(ip , port):
        try:
            sock = socket.create_connection((ip, port), timeout=2)
            sock.close()
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False


def date_and_time():
    cu = datetime.datetime.now()
    time = cu.strftime('%H:%M %p')
    date = datetime.date.today()
    
    return [time , date]



#--------------------main connection------------------------------------
database = mysql.connect(host = "localhost" , user = "root" , passwd = "admin", database = "notmotinfo")
cursor = database.cursor()

#-----------------------------------------------------------------------
def counter(): #counter for id 
    try :
        query = ("SELECT * FROM notinfo WHERE counterpointer = 2024")
        cursor.execute(query)
        for i in cursor :
            (source) = i[6]
        
        query = ("UPDATE notinfo SET counter = %s WHERE counterpointer = %s")
        
        values = (str(int(source) + 1) , "2024")
        cursor.execute(query , values)
        database.commit()
        
        return source
    except Exception as e :
        print(e)
        return False
    

def add_to_db(note , status , cache) :
    try :
        time = date_and_time()[0]
        date = date_and_time()[1]
        query = ("INSERT INTO notinfo(id , note , time , date , status , cache , counter , counterpointer) VALUES(%s , %s , %s , %s , %s , %s , 0 , 0)") #table name <---------------
        id = counter()
        values = (id , note , str(time) , str(date) , status , cache)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    
def del_from_db(id) :
    try :
        query = ("DELETE FROM notinfo WHERE id = %s and id = %s") #table name <---------------
        values = (id , id) #im copy that bc sql have bug 
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e :
        print(e)
        return False
    

def show_data_from_db():
    try :
        query = ("SELECT * FROM notinfo WHERE cache = 0") #table name <--------------
        cursor.execute(query)
        data = []
        for i in cursor :
            data.append(i)
        return data
    except Exception as e :
        print(e)
        return False


def show_cache_data_from_db():
    try :
        query = ("SELECT * FROM notinfo WHERE cache = 1") #table name <--------------
        cursor.execute(query)
        data = []
        for i in cursor :
            data.append(i)
        return data
    except Exception as e :
        print(e)
        return False


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
    

def switch_cache_status_on_db(id , cache):
    try :
        query = ("UPDATE notinfo SET cache = %s WHERE id = %s") #table name <--------------
        values = (cache , id)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception :
        return False


# id | note | time | date | status | cache | counter = 0 | counterpointer = 0  
    
# print(switch_cache_status_on_db(5 , 1))
# # print(show_cache_data_from_db())
print(add_to_db("gym" , "1" , "0" ))
# print(del_from_db(3))
# print(show_cache_data_from_db())
print(show_data_from_db())
