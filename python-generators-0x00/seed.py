import mysql.connector
import csv
class Seed:
    def __init__(self, host, user, password, port=3306):
        self.host = host 
        self.user = user 
        self.port = port
        self.password = password 
    
    def connect_db(self):
        print(f"Connecting to database at {self.host} with user {self.user}...")
        db  = mysql.connector.connect(
            host= self.host, 
            user = self.user, 
            password= self.password, 
            port = self.port
            )

        if not db.is_connected():
            raise Exception("Failed to connect to the database.")
        return db

    def create_database(self,connection):
        try:
            myConnection = connection.cursor()
            myConnection.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        finally:
            myConnection.close()

    def connect_to_prodev(self):
        print("Connecting to ALX_prodev database...")
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database="ALX_prodev"
        )
        return db
    
    def create_table(self, connection):
        try:
            myConnection = connection.cursor()
            myConnection.execute("""
                 CREATE TABLE IF NOT EXISTS user_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    age INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        finally:
            myConnection.close()


            
    def insert_data(self, connection, data):
        myConnection  = connection.cursor()


        with open(data, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                name, email, age = row[0], row[1], int(row[2])
                myConnection.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                if myConnection.fetchone() is None:
                    myConnection.execute(
                        "INSERT INTO user_data (name, email,age,created_at) VALUES (%s, %s,%s,NOW())",
                        (name, email,age)
                    )
                    connection.commit()
        myConnection.close()
        





