# DSC 510
# Week 12
# Programming Assignment Week 12
# Auther: Joaquin Cordero
# 5/20/2024
# This program will look up the weather based on user input of city of zip
# ---------------------------------------------------
import requests


def city_state_cleanup(user_city_state):
    user_city_list = []

    user_city_state = user_city_state.replace(',', ' ')
    user_city_state = user_city_state.strip()
    user_city_list = user_city_state.split()

    user_city_list[-1] = user_city_list[-1].strip(' ').upper() # State will follow after the comma
    user_state = user_city_list.pop()
    separator = " "
    user_city = separator.join(user_city_list)

    city_state_lookup(user_city, user_state)
    # This function will clean up the city/state input from the user


def zip_lookup(user_zip):
    geo_code_url = ("http://api.openweathermap.org/geo/1.0/zip?zip=" + str(user_zip)
                    + ",US&appid=7b828daceb771cb0c3ae432bb66b9948")

    try:
        geo_response = requests.request("GET", geo_code_url)
    except ConnectionError:
        print("There was a connection error.")

    geo_code = geo_response.json()

    for key in geo_code:
        if key == 'lat':
            lat = geo_code[key]
        elif key == 'lon':
            lon = geo_code[key]

    weather_lookup(lat, lon)
    # This function will look up the lat & lon based on user zip code


def city_state_lookup(user_city, user_state):
    city_state_url = ("http://api.openweathermap.org/geo/1.0/direct?q=" + str(user_city) + "," + str(user_state) +
                      ",US&appid=7b828daceb771cb0c3ae432bb66b9948")

    try:
        city_state_response = requests.request("GET", city_state_url)
    except ConnectionError:
        print("There was an connection error.")

    city_state = city_state_response.json()

    for n in city_state:
        for key in n:
            if key == 'lat':
                lat = n[key]
            elif key == 'lon':
                lon = n[key]

    weather_lookup(lat, lon)
    '''
    This function will look up lat & lon from the user city/state from the cleaned up string 
    using the function 'city_state_cleanup'
    '''


def weather_lookup(lat, lon):

    while True:
        user_unit_measurement = input("Please enter the unit measurement('C' for Celsius, "
                                      "'F' for Fahrenheit, 'K' for Kelvin'): ").lower()

        if user_unit_measurement == 'c':
            unit = 'metric'
            break
        elif user_unit_measurement == 'f':
            unit = 'imperial'
            break
        elif user_unit_measurement == 'k':
            unit = ''
            break
        else:
            print("Please enter a unit of measurement.")

    weather_url = ("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) +
                   "&appid=7b828daceb771cb0c3ae432bb66b9948&units=" + unit)

    try:
        weather_response = requests.request("GET", weather_url)
    except ConnectionError:
        print("There was a connection error.")

    weather_info = weather_response.json()

    pretty_print(weather_info, user_unit_measurement)
    # This function will look up the weather info using the lat & lon from the user input of city/state or zip code


def pretty_print(weather_info, user_unit_measurement):
    for key in weather_info:
        if key == 'main':
            for n in weather_info[key]:
                if n == 'temp':
                    temp = (f'{weather_info[key][n]}\xb0' + str(user_unit_measurement).upper())
                elif n == 'feels_like':
                    feels_like_temp = (f'{weather_info[key][n]}\xb0' + str(user_unit_measurement).upper())
                elif n == 'temp_min':
                    temp_min = (f'{weather_info[key][n]}\xb0' + str(user_unit_measurement).upper())
                elif n == 'temp_max':
                    temp_max = (f'{weather_info[key][n]}\xb0' + str(user_unit_measurement).upper())
                elif n == 'humidity':
                    humidity = (str(weather_info[key][n]) + '%')
                elif n == 'pressure':
                    pressure = ((weather_info[key][n]) * 0.02952998057228486)
        elif key == 'name':
            city = (weather_info[key])
        elif key == 'weather':
            for n in weather_info[key]:
                for i in n:
                    if i == 'description':
                        current_weather_description = n[i]

    print("------------------------------------------------")
    print(f'{city + " City": ^45}')
    print(f'{temp: ^45}')
    print(f'{current_weather_description: ^45}')
    print(f'{"Feels like: " + feels_like_temp: ^45}')
    print(f'{"H:" + temp_max + "  L:" + temp_min: ^45}')
    print(f'{"Humidity: " + humidity: ^45}')
    print(f'{"Pressure:" + f'{pressure: .2f}' + "inHg": ^45}')
    print("------------------------------------------------")
    # This function will make the json data readable for the user


def main():
    welcome_message = "Hello! How would you like to look up the weather in your area?"
    print(welcome_message)

    while True:
        city_or_zip = input("Please enter 'c' for city, 'z' for zip code, or 's' to stop: ").lower()

        if city_or_zip == 'c':
            user_city_state = input("Please enter the name of the city and state (Ex: Irvine, CA): ").lower()
            city_state_cleanup(user_city_state)

        elif city_or_zip == 'z':
            user_zip = int(input("Please enter your zip code: "))
            zip_lookup(user_zip)

        elif city_or_zip == 's':
            print("Thank you!")
            break

        else:
            print('Please enter a valid input for city or zip\n')
            continue


if __name__ == '__main__':
    main()
