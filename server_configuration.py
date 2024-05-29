import mysql.connector as mysql

def step1():
    connector = mysql.connect(host="localhost",
                              user="root",
                              passwd="admin")
    
    cursor = connector.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS notmotinfo")
    cursor.close()
    connector.close()

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
        VALUES (0, 'c', 'c', 'c', 'c', '2', '1', 'a')
    """)
    
    connector.commit()
    cursor.close()
    connector.close()

step1()
step2()

print("created")
