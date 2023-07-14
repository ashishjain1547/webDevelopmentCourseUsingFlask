from flask import Flask
from flask import render_template

import sqlite3

# Intializing the Flask app instance
app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('../db/mydb.db')

    cursor = conn.execute("SELECT * FROM cars_and_bikes")

    cars_and_bikes_list = []

    for row in cursor:
        temp_dictionary = {}

        temp_dictionary.update({ "sno" : row[0] })
        temp_dictionary.update({ "brand" : row[1] })
        temp_dictionary.update({ "model" : row[2] })
        temp_dictionary.update({ "year_of_manufacturing" : row[3] })
        temp_dictionary.update({ "price" : int(row[4]) })
        temp_dictionary.update({ "car_or_bike" : row[5] })
        
        cars_and_bikes_list.append(temp_dictionary)

    conn.close()

    return render_template('inventory.html', cars_and_bikes_list=cars_and_bikes_list)

if __name__ == '__main__':
    app.run(port='5000')