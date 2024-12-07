# DSC 510
# Week 10
# Programming Assignment Week 10
# Auther: Joaquin Cordero
# 5/14/2024
# This program will
# ---------------------------------------------------

import requests
from pprint import pprint


def main():

    url = "http://www.boredapi.com/api/activity/"

    try:
        response = requests.request("GET", url)
    except ConnectionError:
        print("There was a connection issue")

    # print(type(response.json()))
    # pprint(response.json())

    activities = response.json()

    # print(activities['activity'])
    # print(activities['type'])

    for key, value in response.json().items():
        print(key, ":", value)


if __name__ == "__main__":
    main()