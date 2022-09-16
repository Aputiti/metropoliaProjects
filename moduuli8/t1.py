import mysql.connector

connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='aputiti',
                                     password='apu123', autocommit=True)


def get_data(icao_code):
    sql_code = "SELECT name, municipality FROM airport WHERE ident = '" + icao_code + "'"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchall()
    if cursor_test.rowcount > 0:
        for row in sql_print:
            print(f"Airport name: {row[0]}\nMunicipality: {row[1]}")
    return


user_icao = input("Insert airport ICAO-code: ")
get_data(user_icao)
