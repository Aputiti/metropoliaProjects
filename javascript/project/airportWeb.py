import json
import mysql.connector
from flask import Flask
from flask_cors import CORS
from geopy.geocoders import Nominatim

connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='YOUR-USERNAME',
                                     password='YOUR-PASSWORD', autocommit=True)

APIKEY = "YOUR-APIKEY-HERE"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

geolocator = Nominatim(user_agent="geoAPI", timeout=3)


@app.route('/continent/<cont_name>')
def get_continent_countries(cont_name):
    sql_code = "SELECT name FROM country WHERE continent = '" + cont_name + "' ORDER BY country.name asc"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchall()

    answer = {
        "Name": sql_print
    }

    return answer


@app.route('/country/<country_name>')
def get_country_airports(country_name):
    sql_code = "SELECT airport.name FROM airport, country WHERE country.iso_country = airport.iso_country " \
               "and country.name = '" + country_name + "' ORDER BY airport.name asc"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchall()

    answer = {
        "Airport": sql_print
    }

    return answer


@app.route('/airport/<airport_name>/<country_name>')
def get_airport_data(airport_name, country_name):
    sql_code = "SELECT * FROM airport, country WHERE airport.name = '" + airport_name + \
               "' and airport.iso_country = country.iso_country and country.name = '" + country_name + "'"
    cursor_test = connection.cursor()
    cursor_test.execute(sql_code)
    sql_print = cursor_test.fetchall()

    answer = {
        "DataTest": sql_print
    }

    return answer


@app.route('/geo/<lat>/<long>')
def get_geo_data(lat, long):
    location = geolocator.reverse(lat + "," + long)

    answer = {
        "Data": str(location)
    }

    return answer


@app.route('/img/<lat>/<long>')
def get_img(lat, long):
    image = 'https://maps.googleapis.com/maps/api/staticmap?center=' + lat + '%2C' + long \
            + '&zoom=14&scale=1&size=280x280&maptype=satellite&format=png&key=' + APIKEY

    answer = {
        "Image": str(image)
    }

    return answer


if __name__ == '__main__':
    app.run(use_reloader=True, host='localhost', port=3000)
