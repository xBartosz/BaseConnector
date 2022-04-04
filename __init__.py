import mysql.connector

class Connector:
    def __init__(self, user, password, host, base_name):
        self.connection = mysql.connector.connect(user=user, password=password, host=host, database=base_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()