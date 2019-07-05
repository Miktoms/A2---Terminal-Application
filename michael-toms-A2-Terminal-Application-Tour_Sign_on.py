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

def day():
    da = input(f'what day of the month were you born on')
    return da

def month():
    mo = input(f'and what number is the month of your birth, please type Month like JAN, FEB etc')
    return mo

def year():
    ye = input(f'lastly, What is the year of your birth')
    return ye

def dob():
    date = day(),month(),year()
    return date

name = get_name()
date = dob()

allergy()

print(name)
print(date)