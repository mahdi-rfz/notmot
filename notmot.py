import mysql.connector as mysql
from colorama import Fore
import socket
import argparse
import requests
import time 
import os


#Enter database information
"""
datebase name =
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
    



#--------------------main connection------------------------------------
database = mysql.connect(host = "localhost" , user = "root" , passwd = "admin", database = "notmotinfo")
cursor = database.cursor()

#-----------------------------------------------------------------------

def add_to_db(id , note , time , date , status , cache) :
    try :
        query = ("INSERT INTO notinfo(id , note , time , date , status , cache) VALUES(%s , %s , %s , %s , %s , %s)") #table name <---------------
        values = (id , note , time , date , status , cache)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception as e :
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
    
    
# print(switch_cache_status_on_db(41 , 0))
# # print(show_cache_data_from_db())
# # print(add_to_db(56 , 1234 , 44 , 4525323 , 1 , 1))
# print(del_from_db(56))
# print(show_cache_data_from_db())
# print(show_data_from_db())