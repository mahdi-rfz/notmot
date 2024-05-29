import mysql.connector as msql
from colorama import Fore
import socket
import argparse
import requests
import time 
import os


#Enter database information
host = () # enter ip or etc
user = () # enter database username
passwd = () # enter database password
database = () # enter databse name for creat connection 
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

dbconnection = msql.connect(host , user , passwd , database)
cursor = dbconnection.cursor()

#-----------------------------------------------------------------------

def add_to_db(id , note , time , date , status , cache) :
    try :
        query = ("INSERT INTO notmotinfo(id , note , time , date , status , cache) VALUES(%s , %s , %s , %s , %s , %s)") #table name <---------------
        values = (id , note , time , date , status , cache)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception :
        return False
    
    
def del_from_db(id) :
    try :
        query = ("DELETE FROM notmotinfo WHERE id = %s") #table name <---------------
        values = (id)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception :
        return False
    

def show_data_from_db():
    try :
        query = ("SELECT * FROM notmotinfo WHERE cache = 0") #table name <--------------
        cursor.execute(query)
        data = []
        for i in cursor :
            data.append(i)
        return data
    except Exception :
        return False


def show_cache_data_from_db():
    try :
        query = ("SELECT * FROM notmotinfo WHERE cache = 1") #table name <--------------
        cursor.execute(query)
        data = []
        for i in cursor :
            data.append(i)
        return data
    except Exception :
        return False

def switch_status_on_db(id , status):
    try :
        query = ("UPDATE human SET status = %s WHERE id = %s") #table name <--------------
        values = (status , id)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception :
        return False
    

def switch_cache_status_on_db(id , cache):
    try :
        query = ("UPDATE human SET cache = %s WHERE id = %s") #table name <--------------
        values = (cache , id)
        cursor.execute(query , values)
        database.commit()
        return True
    except Exception :
        return False