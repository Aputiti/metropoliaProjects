import mysql.connector
from flask import Flask

connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='YOUR-USERNAME-HERE',
                                     password='YOUR-PASSWORD-HERE', autocommit=True)

app = Flask(__name__)


@app.route('/airport/<icao_code>')
def get_data(icao_code):
    sql_code = "SELECT name, municipality FROM airport WHERE ident = '" + icao_code + "'"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchall()

    answer = {
        "ICAO": icao_code,
        "Name": sql_print[0][0],
        "Municipality": sql_print[0][1]
    }

    return answer


if __name__ == '__main__':
    app.run(use_reloader=True, host='localhost', port=3000)
