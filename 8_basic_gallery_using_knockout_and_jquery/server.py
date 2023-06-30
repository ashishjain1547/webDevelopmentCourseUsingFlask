from flask import Flask
from flask import render_template

import sqlite3

from flask_bootstrap import Bootstrap

# Intializing the Flask app instance
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    conn = sqlite3.connect('cars_images.db')

    cursor = conn.execute("SELECT * FROM cars_img")

    l = []

    for row in cursor:
        temp_dictionary = {}

        temp_dictionary.update({ "brand" : row[0] })
        temp_dictionary.update({ "model" : row[1] })
        temp_dictionary.update({ "year" : row[2] })
        temp_dictionary.update({ "img" : row[3] })
        
        l.append(temp_dictionary)

    conn.close()

    return render_template('inventory.html', cars_list=l)

if __name__ == '__main__':
    app.run(port='5000')