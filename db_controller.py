import psycopg2 as postgres

connector = postgres.connect(
        dbname="your_database",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )

cursor = connector.cursor()

class Postgresql_connector:
    def __init__(self):
        pass

    def add_to_db(text) :
        pass
    
    def del_from_db(id) :
        pass
    
    def show_data_from_db(id) :
        pass
    
    def switch_planer_status(id):
        pass
    
    def check_status(id):
        pass
    
    