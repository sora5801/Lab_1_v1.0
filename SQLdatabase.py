import sqlite3
import re

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
                # print("The SQLite connection is closed")

    def Fetch(self, condb, nm):
        cursorObj = self.sqliteConnection.cursor()
        self.sqliteConnection.cursor()
        sel = 'SELECT id FROM {0} WHERE name == "{1}"'.format(condb, nm)
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)

    def Table(self):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            sqlite_create_table_query = '''CREATE TABLE Database (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            photo text NOT NULL UNIQUE,
                                            html text NOT NULL UNIQUE);'''

            cursor = self.sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            self.sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (self.sqliteConnection):
                self.sqliteConnection.close()
                # print("sqlite connection is closed")

    def readSqliteTable(self):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_select_query = """SELECT * from Database"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))
            print("Printing each row")
            for row in records:
                print("id: ", row[0])
                print("name: ", row[1])
                print("photo: ", row[2])
                print("html: ", row[3])
                print("\n")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("The SQLite connection is closed")

    def deleteRecord(self):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
            print("Connected to SQLite")

            # Deleting single record now
            sql_delete_query = """DELETE from Database where id = 2"""
            cursor.execute(sql_delete_query)
            self.sqliteConnection.commit()
            print("Record deleted successfully ")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("the sqlite connection is closed")

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def insertBLOB(self, empId, name, photo, resumeFile):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_insert_blob_query = """ INSERT INTO Database
                                          (id, name, photo, html) VALUES (?, ?, ?, ?)"""

            empPhoto = self.convertToBinaryData(photo)
            resume = self.convertToBinaryData(resumeFile)
            # Convert data into tuple format
            data_tuple = (empId, name, empPhoto, resume)
            cursor.execute(sqlite_insert_blob_query, data_tuple)
            self.sqliteConnection.commit()
            print("Image and file inserted successfully as a BLOB into a table")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("the sqlite connection is closed")

    def updateSqliteTable(self, id, htext):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
            print("Connected to SQLite")

            sql_update_query = """Update Database set html = ? where id = ?"""
            data = (htext, id)
            cursor.execute(sql_update_query, data)
            self.sqliteConnection.commit()
            print("Record Updated successfully")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("The sqlite connection is closed")

    def DeleteDatabase(self):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            sqlite_create_table_query = """DROP TABLE Database"""

            cursor = self.sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            self.sqliteConnection.commit()
            print("Database deleted")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while deleting database", error)

        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("sqlite connection is closed")

    def __getitem__(self, year):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
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
                        if(year == float(x[0])):
                            return float(x[1])
                            break;

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

        finally:
            if (self.sqliteConnection):
                self.sqliteConnection.close()
                print("The SQLite connection is closed")
