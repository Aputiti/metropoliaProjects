import mysql.connector

connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='aputiti',
                                     password='apu123', autocommit=True)


def get_data(iso):
    sql_code = "SELECT type, count(*) FROM airport WHERE iso_country = '" + iso +\
               "' GROUP BY type ORDER BY count(*) desc"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchall()
    if cursor_test.rowcount > 0:
        for row in sql_print:
            print(f"{row[0]}: {row[1]}")
    return


user_iso = input("Insert country code: ")
get_data(user_iso)
