from geopy import distance
import mysql.connector

connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='aputiti',
                                     password='apu123', autocommit=True)


def airport_latitude(icao):
    sql_code = "SELECT latitude_deg FROM airport WHERE ident = '" + icao + "'"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchone()
    return sql_print[0]


def airport_longitude(icao):
    sql_code = "SELECT longitude_deg FROM airport WHERE ident = '" + icao + "'"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchone()
    return sql_print[0]


user_iso_1 = input("First airport ICAO: ")
user_iso_2 = input("Second airport ICAO: ")

first_airport_location = (airport_latitude(user_iso_1), airport_longitude(user_iso_1))
second_airport_location = (airport_latitude(user_iso_2), airport_longitude(user_iso_2))

airports_distance = distance.distance(first_airport_location, second_airport_location).km
print(f"Distance between the airports is {airports_distance:.3f} kilometers.")
