import sqlite3

"""
in nots.db : 
id , username , note , time , date


in users.db : 
username , password(hash) 


in logs.db : 
username , ip , time , date
"""

class Tool:
    def __init__(self , username , note):
        self.username = username
        self.note = note
    
    def addNote(self):
        connection = sqlite3.connect("nots.db")
        cursor = connection.cursor()

    def delNote(self):
        connection = sqlite3.connect("nots.db")
        cursor = connection.cursor()


    def showNote(self):
        connection = sqlite3.connect("nots.db")
        cursor = connection.cursor()


class UserValidation:
    def __init__(self , username , password):
        self.username = username 
        self.password = password