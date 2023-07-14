from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'


# This is the landing page to the site.
# Upon landing here, the user will see a form.
# If you would open and see in form.html, there is this piece of string present:
# <form action="http://127.0.0.1:9000/insert_record" method="POST" enctype="multipart/form-data">
# This tells the once the form is submitted, it has to be processed by "insert_record" handle (in server.py file).
# Inside "insert_record" function, we read different inputs coming as part of request. 
# And pass these different inputs as arguments to the next function to form an SQL query and execute it.
# 
# When a request comes, it has a source. When it was coming on click of a link, submission of a form, or an AJAX request. 
#
# The next function to form an SQL query is: insert_into_car_company
# After a record in inserted, we want to show a message to the user. 
# This message appears on template "form_response.html".


@app.route('/')
def index():
    return render_template('form.html')


@app.route("/insert_record", methods=['POST'])
def insert_record():

    print("Content-Type: " + request.headers['Content-Type'])

    if "multipart/form-data;" in request.headers['Content-Type']:

        company_name = request.form.get("ccn")
        headquarter = request.form.get("headquarter")
        founded_in = request.form.get("founded_in")
        founder = request.form.get("founder")
        
        rtn = insert_into_car_company(company_name, headquarter, founded_in, founder)

    else:
        return "415 Unsupported Media Type"

    if rtn:
        msg = "Record added successfully."
    else:
        msg = "Failed to add record."

    return render_template('form_response.html', msg=msg)

def insert_into_car_company(company_name, headquarter, founded_in, founder):
    rtn = True

    try:
        sqliteConnection = sqlite3.connect('car_companies.db')
        cursor = sqliteConnection.cursor()
        

        sqlite_insert_query = """INSERT INTO car_company
                            (company_name, headquarter, founded_in, founder) 
                            VALUES 
                            ('{}', '{}', {}, '{}')""".format(company_name, headquarter, founded_in, founder)

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()

        print("Record inserted successfully into table ", cursor.rowcount)
        
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
        rtn = False 

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

    return rtn


@app.route('/viewAllCompanies')
def view_all():

    conn = sqlite3.connect('car_companies.db')

    cursor = conn.execute("SELECT * FROM car_company")

    car_companies = []

    for row in cursor:
        temp_dictionary = {}

        temp_dictionary.update({ "company_name" : row[0] })
        temp_dictionary.update({ "headquarter" : row[1] })
        temp_dictionary.update({ "founded_in" : row[2] })
        temp_dictionary.update({ "founder" : row[3] })
        
        
        car_companies.append(temp_dictionary)

    conn.close()

    return render_template('view_all_companies.html', car_companies=car_companies)



if __name__ == "__main__":
    app.run(port = 9000)