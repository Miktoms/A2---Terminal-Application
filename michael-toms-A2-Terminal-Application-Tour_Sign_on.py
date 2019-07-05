#!/usr/bin/python3
'''
Author Michael J Toms
contact:css0119020@coderacademy.edu.au
date 28/06/2019
Licence GPLv3
Version 0.1
'''
def get_name():

    name = input("Enter your name: ")

    print(f'Hello {name}, Welcome to the Tour')
    return name

def allergy():

    allergy_values = ['Y', 'N','YES','NO']
    allergy = input('Do you have a food allergy? (Y/N)')

    while allergy.upper() not in allergy_values:
        print("Please enter Y or N")
        allergy = input('Do you have a food allergy? (Y/N) ')

    if allergy.upper() == "N":
        print('Welcome to the tour, as you have no food allergies you can enjoy all of the food on offer')
    else:
        specific_allergy = input("What sort of allergy do you have? ")
        print(f'We see that you have an allergy called: {specific_allergy}, we\'ll make sure that you\'re catered for')

def get_day():
    r = range(1,32)
    while True:
        try:
            day = int(input(f'what day of the month were you born on'))
        except ValueError:
            print('Please enter a number from 1-31: ')
            continue
        if day not in r:
            print('Please enter a number from 1-31')
            continue 
        return day

def get_month():
    r = range(1,13)
    while True:
        try:
            month = int(input(f'and what number is the month of your birth, 1-12?'
))
        except ValueError:
            print('Please enter a number from 1-12: ')
            continue
        if month not in r:
            print('Please enter a number from 1-12')
            continue
        return month
def get_year():
    r = range(0,3000)
    while True:
        try:
            year = int(input(f'Lastly, what year were you born in'))
        except ValueError:
            print('Please enter a valid year:')
            continue
        if year not in r:
            print('Please enter a valid year')
            continue 
        return year
def dob():
    date = get_day(),get_month(),get_year()
    return date
name = get_name()
date = dob()
allergy()
print(name)
print(f'and because your dob is {date}')