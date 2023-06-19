from flask import Flask

import sqlite3

# Intializing the Flask app instance
app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('../db/mydb.db')

    cursor = conn.execute("SELECT * FROM cars_and_bikes")

    html_str = """<table>
        <tr>
            <td>Sno</td>
            <td>Brand</td>
            <td>Model</td>
            <td>Year of Manufacturing</td>
            <td>Price</td>
            <td>Car or Bike</td>
        </tr>
        """

    for row in cursor:
        row_str = "<tr>"
        row_str += "<td>" + str(row[0]) + "</td>"
        row_str += "<td>" + str(row[1]) + "</td>"
        row_str += "<td>" + str(row[2]) + "</td>"
        row_str += "<td>" + str(row[3]) + "</td>"
        row_str += "<td>" + str(row[4]) + "</td>"
        row_str += "<td>" + str(row[5]) + "</td>"
        row_str += "</tr>"

        html_str += row_str
    
    html_str += """ </table> """

    conn.close()

    return html_str

if __name__ == '__main__':
    app.run(port='5000')