
import sqlite3

class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.__instances[cls]

class Database(metaclass=Singleton):
    
    connection = None

    def coonnect(self):
        if self.connection is None:
            print(f"Não temos ainda uma conexão... vamos criá-la...")
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = Database().coonnect()
db2 = Database().coonnect() 
