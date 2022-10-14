# This is a project for Ohjelmisto 1 -course in Metropolia University of Applied Sciences. (FULL PROJECT WITH GUI)

# Authors: Abdur Abou Ramadan, Ahmed Ezzaroui, Juan Rosales and Sami Abo Ramadan.

# Last edit done on 13.10.2022.

"""
--> IN ORDER TO USE THIS PROGRAM YOU NEED GEOPY, PILLOW, REQUESTS AND "GOOGLEMAPS" LIBRARY, A PLACEHOLDER PHOTO,
--> CORRECT IMAGE FILE PATH(S), THE RIGHT AIRPORT DATABASE (FLIGHT_GAME) CONNECTED AND A WORKING GOOGLE API KEY.
--> IF YOU DON'T HAVE A GOOGLE API KEY THE PICTURE PART OF THE PROGRAM WON'T WORK AND YOU WILL BE MET WITH ERRORS.
"""

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from geopy.geocoders import Nominatim
import requests


# ---CLEANUP PYCHARM


# connecting to database - USE YOUR OWN LOGIN DETAILS IN ORDER TO WORK CORRECTLY
connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='aputiti',
                                     password='apu123', autocommit=True)

continent_chosen = 0
user_continent = "N/A"
country_chosen = 0
user_country = "N/A"
lat = "N/A"
long = "N/A"

API_KEY = 'AIzaSyDmKMxviK5Ko5HOaVKglXa2XxFCHedrm2g'

geolocator = Nominatim(user_agent="geoAPI", timeout=3)


# function to check user continent choice
def choose_continent():
    if (user_entry.get() == "AF" or user_entry.get() == "AN" or user_entry.get() == "AS" or user_entry.get() == "EU" or
            user_entry.get() == "NA" or user_entry.get() == "SA" or user_entry.get() == "OC"):
        global user_continent
        user_continent = user_entry.get()
        global continent_chosen
        continent_chosen = 1
        command_label.config(text="Choose a country")
        user_label.config(text=user_entry.get() + "!", fg='green')
    else:
        user_label.config(text="Error!", fg='red')


# function to check if the chosen country is in the formerly selected continent
def check_country(ctry, cont):
    sql_code = "SELECT iso_country FROM country WHERE name = '" + ctry + "' and continent = '" + cont + "'"
    cursor = connection.cursor()
    cursor.execute(sql_code)
    cursor.fetchall()
    return cursor.rowcount


# function to get all the different airports in the chosen country
def get_airport_names(ctry):
    if check_country(user_entry.get(), user_continent) == 1:
        sql_code = "SELECT airport.name FROM airport, country WHERE country.iso_country = airport.iso_country" \
                   " and country.name = '" + ctry + "' ORDER BY airport.name asc"
        cursor = connection.cursor()
        cursor.execute(sql_code)
        sql_print = cursor.fetchall()
        if cursor.rowcount > 0:
            list_box.delete(0, END)
            command_label.config(text="Choose an airport")
            for row in sql_print:
                list_box.insert(END, row[0])
            get_airports_amount(user_entry.get())
            get_airports_total(user_entry.get())
            user_label.config(text=user_entry.get().capitalize() + "!", fg='green')
            global user_country
            user_country = user_entry.get().capitalize()
            global country_chosen
            country_chosen = 1
        else:
            user_label.config(text="Error!", fg='red')
    else:
        user_label.config(text="Error!", fg='red')
    return


# function to get the amount of different airports in the chosen country
def get_airports_amount(ctry):
    sql_code = "SELECT type, count(*) FROM airport, country WHERE country.iso_country = airport.iso_country " \
               " and country.name = '" + ctry + "' GROUP BY type ORDER BY count(*) desc"
    cursor = connection.cursor()
    cursor.execute(sql_code)
    sql_print = cursor.fetchall()
    if cursor.rowcount > 0:
        data_text.config(state=NORMAL)
        data_text.delete(1.0, END)
        for row in sql_print:
            data_text.insert(END, row[0].capitalize() + ": " + str(row[1]) + "\n")
        data_text.config(state=DISABLED)
    return


# function to get the total amount of airports in the chosen country
def get_airports_total(ctry):
    sql_code = "SELECT count(*) FROM airport, country WHERE country.iso_country = airport.iso_country" \
               " and country.name = '" + ctry + "'"
    cursor = connection.cursor()
    cursor.execute(sql_code)
    sql_print = cursor.fetchall()
    data_text.config(state=NORMAL)
    if cursor.rowcount > 0:
        for row in sql_print:
            data_text.insert(END, "\nAirports in total: " + str(row[0]))
    data_text.config(state=DISABLED)
    return


# function to get wanted data from a certain airport
def get_airport_data(name, ctry):
    sql_code = "SELECT * FROM airport, country WHERE airport.name" \
               " = '" + name + "' and airport.iso_country = country.iso_country and country.name = '" + ctry + "'"
    cursor = connection.cursor()
    cursor.execute(sql_code)
    sql_print = cursor.fetchall()
    if cursor.rowcount > 0:
        data_text.config(state=NORMAL)
        data_text.delete(1.0, END)
        user_label.config(text="Airport!", fg='green')
        for row in sql_print:
            data_text.insert(END, "ICAO:-> " + str(row[1]) + "\nType:-> " + str(row[2]) + "\nLatitude:-> "
                             + str(row[4]) + "\nLongitude:-> " + str(row[5]) + "\nElevation:-> "
                             + str(row[6]) + "f\nScheduled service:-> " + str(row[11]) + "\nWikipedia:-> " + str(row[16]))
        global lat
        lat = str(row[4])
        global long
        long = str(row[5])
    else:
        user_label.config(text="Error!", fg='red')
    data_text.insert(END, "\n\nData:-> " + str(location_data(lat, long)))
    data_text.config(state=DISABLED)
    get_photo(lat, long)
    newimg = ImageTk.PhotoImage(
        Image.open("/Users/abdur/PycharmProjects/MetrpoProject1/mainDir/airport_photo.png").resize((200, 200), Image.ANTIALIAS))
    image_label.config(image=newimg)
    image_label.image = newimg
    return


# function to get data from airports location
def location_data(latitude, longitude):
    location = geolocator.reverse(latitude + "," + longitude)
    return location


# function to get the photo of the airport using latitude and longitude and saving it as a png
def get_photo(latitude, longitude):
    url = 'https://maps.googleapis.com/maps/api/staticmap?center=' + latitude + '%2C' + \
          longitude + '&zoom=14&scale=2&size=500x500&maptype=satellite&format=png&key=' + API_KEY
    response = requests.get(url)
    with open('airport_photo.png', 'wb') as file:
        file.write(response.content)
    return


# function to run when clicking enter
def get_user_input():
    if bool(continent_chosen):
        if bool(country_chosen):
            get_airport_data(user_entry.get(), user_country)
        else:
            get_airport_names(user_entry.get())
    else:
        choose_continent()
    return


# creating the root (main window) and setting its size and location on the screen
root = Tk()
root.title('Airport Simulator')
win_width = 600
win_height = 465

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (win_width / 2)
y = (screen_height / 2) - (win_height / 2)

root.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))
root.resizable(False, False)

# creating the instruction window and setting its size and location on the screen
instruction_window = Toplevel(root)
instruction_window.title("Instructions")
ins_width = 450
ins_height = 175

x = (screen_width / 2) - (ins_width / 2)
y = (screen_height / 2) - (ins_height / 2)

instruction_window.geometry('%dx%d+%d+%d' % (ins_width, ins_height, x, y))
# instruction_window.resizable(False, False)

# setting up the instruction window
ins_textbox = Text(instruction_window, height=7, width=60, pady=20, padx=20)
ins_textbox.insert(END, "Welcome to Airport Simulator! You will start by choosing a continent"
                        " ((AF) (AN) (AS) (EU) (NA) (SA) (OC)) and a country that’s located in the chosen"
                        " continent. After that you will be presented with all the airports in that country."
                        " You can then find some interesting data about every individual airport available"
                        " and you will also see a satellite image of the chosen airport.")
ins_button = Button(instruction_window, text='Close', command=instruction_window.destroy)
ins_textbox.config(state=DISABLED)
ins_textbox.pack()
ins_button.pack()

# and now the main window, starting with the widgets
main_frame = Frame(root, cursor='circle')

# left side widgets (top-down)
command_label = Label(main_frame, text='Choose a continent', borderwidth=3, relief='groove', font=('Courier', 18),
                      pady=8, padx=5, width=19, height=1)
command_label.grid(row=0, column=0)

user_entry = Entry(main_frame, font=('Courier', 15))
user_entry.grid(row=1, column=0)

enter_button = Button(main_frame, command=lambda: get_user_input(), text='Enter', width=17)
enter_button.grid(row=2, column=0)

user_label = Label(main_frame, text='Nothing yet!', borderwidth=3, relief='groove', font=('Courier', 18),
                   pady=8, padx=5, width=15, height=1)
user_label.grid(row=3, column=0)

list_box = Listbox(main_frame)
list_scrollbar = Scrollbar(main_frame, bd=4)
list_box.config(yscrollcommand=list_scrollbar.set)
list_scrollbar.config(command=list_box.yview)

placeholder_list = ["Airport name 1", "Airport name 2", "Airport name 3", "Airport name 3", "Airport name 4",
                    "Airport name 5", "Airport name 6", "Airport name 7", "Airport name 8", "Airport name 9",
                    "Airport name 10", "Airport name 11", "Airport name 12", "Airport name 13", "Airport name 14",
                    "Airport name 15"]
for i in placeholder_list:
    list_box.insert(END, i)

list_box.grid(row=4, column=0, pady=15)
list_scrollbar.grid(row=4, column=0, sticky=NS+E, pady=15)

# right side widgets (top-down)
placeholder_img = ImageTk.PhotoImage(Image.open("/Users/abdur/Downloads/worldround.png").resize((200, 200), Image.ANTIALIAS))
image_label = Label(main_frame, image=placeholder_img)
image_label.grid(row=0, column=1, rowspan=4, padx=25)

data_text = Text(main_frame, height=13, width=30)
data_text.insert(END, "\n\n\n\n\n\n    No country chosen yet!")
data_text.config(state=DISABLED)
data_text.grid(row=4, column=1, pady=15)

main_frame.pack(expand=True)
root.mainloop()
