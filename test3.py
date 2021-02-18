from collections import defaultdict
from collections import namedtuple
import sqlite3
import re


class Database:

    def __init__(self):
        self.Temperature = namedtuple('Temperature',
                                      ['median', 'upper', 'lower'])
        self.TemperatureDatabase = defaultdict(lambda: self.Temperature('0', '0', '0'))

    def ReadTemperature(self):  # Read in the temperature file
        with open('Temperature.csv', 'r') as f:
            Temp = f.readlines()[4:-1]
            for line in Temp:
                fields = re.search(
                    r"(\d{4}).*?([-][0]+[.]\d+|[0]+[.]\d+).*?([-][0]+[.]\d+|[0]+[.]\d+|[0]).*?([-][0]+[.]\d+|[0]+["
                    r".]\d+)",
                    line)
                year = fields.group(1)
                Median = float(fields.group(2))
                Upper = float(fields.group(3))
                Lower = float(fields.group(4))
                T = self.Temperature( Median, Upper, Lower)
                self.TemperatureDatabase[year] = T

    def print(self):
        for i in self.TemperatureDatabase.items():
            print(i)

class SQLdatabase:
        def __init__(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Database created and Successfully Connected to SQLite")
                sqlite_select_Query = "select sqlite_version();"
                cursor.execute(sqlite_select_Query)
                record = cursor.fetchall()
                print("SQLite Database Version is: ", record)
                cursor.close()

            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    #print("The SQLite connection is closed")

        def TemperatureDatabase(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = '''CREATE TABLE Temperature (
                                                        year INTEGER PRIMARY KEY,
                                                        median REAL NOT NULL,
                                                        upper REAL NOT NULL ,
                                                        lower REAL NOT NULL );'''

                cursor = self.sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
                #print("SQLite table created")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while creating a sqlite table", error)

            finally:
                if self.sqliteConnection:
                   self.sqliteConnection.close()
                  # print("sqlite connection is closed")

        def readTemperatureTable(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_select_query = """SELECT * from Temperature"""
                cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                print("Total rows are:  ", len(records))
                print("Printing each row")
                for row in records:
                    print("Year: ", row[0])
                    print("Median: ", row[1])
                    print("Upper: ", row[2])
                    print("Lower: ", row[3])
                    print("\n")

                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                    print("The SQLite connection is closed")


        def insertTemperatureData(self):
            DB = Database()
            DB.ReadTemperature()
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = self.sqliteConnection.cursor()
              #  print("Connected to SQLite")
                sqlite_insert_blob_query = """ INSERT INTO Temperature
                                                      (year, median, lower, upper) VALUES (?, ?, ?, ?)"""

                for i in DB.TemperatureDatabase.keys():
                    data_tuple = (int(i), DB.TemperatureDatabase[i].median,
                          DB.TemperatureDatabase[i].lower, DB.TemperatureDatabase[i].upper)
                    cursor.execute(sqlite_insert_blob_query, data_tuple)
                self.sqliteConnection.commit()
              #  print("Temperature datas successfully inserted into the Temperature table")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert temperature data into sqlite table", error)
            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                  #  print("the sqlite connection is closed")



        def DeleteTemperature(self):
            try:
                self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
                sqlite_create_table_query = """DROP TABLE Temperature"""

                cursor = self.sqliteConnection.cursor()
                #print("Successfully Connected to SQLite")
                cursor.execute(sqlite_create_table_query)
                self.sqliteConnection.commit()
               # print("Database deleted")

                cursor.close()

            except sqlite3.Error as error:
                print("Error while deleting database", error)

            finally:
                if self.sqliteConnection:
                    self.sqliteConnection.close()
                   # print("sqlite connection is closed")

class TemperatureDatabase:
    def __init__(self):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                # print("The SQLite connection is closed")
        self.SQ = SQLdatabase()
        self.SQ.TemperatureDatabase()
        self.SQ.insertTemperatureData()
        self.SQ.readTemperatureTable()

def main():
   BE = TemperatureDatabase()

if __name__ == "__main__":
    main()