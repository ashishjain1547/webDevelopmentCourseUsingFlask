from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

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

        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        
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