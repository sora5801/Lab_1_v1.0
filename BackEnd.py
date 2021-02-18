from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import sqlite3
from SQLdatabase import SQLdatabase
import re


class BackEnd:
    def __init__(self):
        self.years = list()  # list for years
        self.median = list()  # list for median
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

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

        finally:
            if (self.SQ.sqliteConnection):
                self.SQ.sqliteConnection.close()
                print("The SQLite connection is closed")

    def search(self, year):
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
                        if(year == float(x[0])):
                            print(float(x[1]))
                            break;

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

        finally:
            if (self.SQ.sqliteConnection):
                self.SQ.sqliteConnection.close()
                print("The SQLite connection is closed")

    def LinearRegression(self):
        a = np.array(self.years).reshape(-1, 1)
        c = np.array(self.median)
        plt.figure(figsize=(13, 10))
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(a, c)  # perform linear regression
        Y_pred = linear_regressor.predict(a)  # make predictions
        plt.scatter(a, c)
        plt.ylabel("Celsius")
        plt.xlabel("Years")
        plt.title("Temperature vs years Linear Regression")
        plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.plot(a, Y_pred, color='red')

        plt.show()

    def XYplot(self):
        # Function to plot
        plt.figure(figsize=(13, 10))
        plt.plot(self.years, self.median, color='red', label='median')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.ylabel("Celsius")
        plt.xlabel("Years")
        plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.title("Temperature vs years XYplot")
        # function to show the plot
        plt.tight_layout()
        plt.show()

    def BarChart(self):
        # Function to plot the bar
        plt.figure(figsize=(13, 10))
        plt.bar(self.years, self.median)
        plt.ylabel("Celsius")
        plt.xlabel("Years")
        plt.title("Temperature vs years BarChart")
        # function to show the plot
        plt.hlines([-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], 1850, 2020, linestyles='dotted')
        plt.show()

# def __del__(self): #The destructor.
# self.SQ.DeleteTemperature() #Destroy the Temperature database to create another one.
# while the program is running, the temperature data will be in database
# When the program ends, the temperature data will be deleted from the database.
#  print("Temperature database deleted.")
