import mysql.connector as mysql
import datetime

"""
run this script on data base server
"""

#creat database 
def step1(): 
    connector = mysql.connect(host="46.4.156.37",
                              user="user",
                              passwd="password")
    
    cursor = connector.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS notmotinfo")
    cursor.close()
    connector.close()


#creat table and culomns
def step2():
    connector = mysql.connect(host="localhost",
                              user="root",
                              passwd="admin",
                              database="notmotinfo")
    
    cursor = connector.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notinfo (
            id INT PRIMARY KEY,
            note TEXT,
            time VARCHAR(50),
            date VARCHAR(50),
            status VARCHAR(50),
            cache VARCHAR(255),
            counter TEXT,
            counterpointer VARCHAR(50)
        )
    """)
    

    cursor.execute("""
        INSERT INTO notinfo (id, note, time, date, status, cache, counter, counterpointer)
        VALUES (0, 'c', 'c', 'c', 'c', '2', '1', '2024')
    """)
    
    connector.commit()
    cursor.close()
    connector.close()

step1()
step2()

cu = datetime.datetime.now()
time = cu.strftime('%H:%M %p')
    
print(f"::::::::::(Database was created)::({time})::::::::::")
