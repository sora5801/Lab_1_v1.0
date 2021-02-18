import sqlite3
from SQLdatabase import SQLdatabase
import re


class Database:
    def __init__(self):
        self.years = list()  # list for years
        self.median = list()  # list for median
        self.upper = list()
        self.lower = list()
        self.SQ = SQLdatabase()
        self.SQ.Table()
        self.SQ.insertBLOB(1, "Temperature", "Temperature.png", "Temperature.html")
        try:
            self.SQ.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.SQ.sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_select_query = """SELECT html from Database"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            for row in records:
                for i in row:
                    fields = re.findall( #Using findall because i is actually one line
                        r"(\d{4}).*?([-][0]+[.]\d+|[0]+[.]\d+).*?([-][0]+[.]\d+|[0]+[.]\d+|[0]).*?([-][0]+[.]\d+|[0]+["
                        r".]\d+)",
                        i.decode(
                            "utf-8"))  # Needed because i is in bytes. Using the decode function to turn i into string
                    for x in fields:
                        self.years.append(float(x[0]))
                        self.median.append(float(x[1]))
                        self.upper.append(float(x[2]))
                        self.lower.append(float(x[3]))

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

def main():
   BE = Database()

if __name__ == "__main__":
    main()