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
    



#--------------------main------------------------------------

dbconnection = msql.connect(host , user , passwd , database)
cursor = dbconnection.cursor()

