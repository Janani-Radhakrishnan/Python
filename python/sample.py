import mysql.connector
class Database:
    def __init__(self, host, user, password):
        try:
           self.connection = mysql.connector.connect(
               host = host,
               user = user,
               password = password
           )
           self.cursor = self.connection.cursor()
           print("Connection to MySQL server established.")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL server: {e}")
            self.connection = None
            self.cursor = None
    def show_databases(self):
        if self.cursor:
            self.cursor.execute("SHOW DATABASES")
            print("Databases:")
            for db in self.cursor:
                print(db)
    def create_database(self, db_name):
        if self.cursor:
            try:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"Database '{db_name}' created or already exists.")
            except mysql.connector.Error as e:
                print(f"Error creating database '{db_name}': {e}")
    def use_database(self, db_name):
        try:
            self.connection.database = db_name
            print(f"Switched to database '{db_name}'.")
        except mysql.connector.Error as e:
            print(f"Error switching to database '{db_name}': {e}")
    def create_table(self, table_name, schema):
        if self.cursor:
            try:
                self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
                print(f"Table '{table_name}' created or already exists.")
            except mysql.connector.Error as e:
                print(f"Error creating table '{table_name}': {e}")
    def insert_data(self, table_name, columns, values):
        if self.cursor:
            try:
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                self.cursor.execute(query)
                self.connection.commit()
                print(f"Data inserted into '{table_name}': {values}")
            except mysql.connector.Error as e:
                print(f"Error inserting data into table '{table_name}': {e}")
    def fetch_data(self, table_name):
        if self.cursor:
            try:
                self.cursor.execute(f"SELECT * FROM {table_name}")
                results = self.cursor.fetchall()
                print(f"Data in '{table_name}':")
                for row in results:
                    print(row)
            except mysql.connector.Error as e:
                print(f"Error fetching data from table '{table_name}': {e}")
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")








