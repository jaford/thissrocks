import python_weather
import asyncio
import os
import sys, signal
import pandas as pd
sys.path.append('..')
from datetime import datetime
from termios import tcflush, TCIFLUSH
from functions.weatherData import getWeather
from functions.dataCompile import dataFormating
from functions.feh2celConv import feh2cel
from functions.progressBar import loadBar
from functions.sendEmail import sendMail
from functions.lineRemove  import deleteLastLine
from functions.excelConv import excelConv

while True:
    introText = '\n---- Welcome to my Weather Program! ----\n\n----How to use----\n'\
        'Step 1: Enter the city in which you want to see the weather in.\n'\
        'Step 2: Convert the tempatures into celsius if you want to see both displayed.\n'\
        'Step 3: Select to see if you want to information to display on your terminal or sent as email to yourself. (AKA ME AS OF NOW)\n'\
        '\n---- Current issues/upcoming features ----\n'\
        'Add to where you can enter the cities name\nCreate unit test to for my program to better run testing. (Create random values for the lists/dictionaries)\n'\
        'Have a enterable email (Sender & reciver)\nAdd color logging at a later point!\n'\
    
    print(introText)
    userInput = input('Are you ready to start? (Y/N)\n').lower().strip()
    lineAmount = len(userInput.splitlines() + introText.splitlines())
    deleteLastLine(lineAmount)
    if userInput == 'y':
        while True: 
                print('Use "Albuquerque" as an example.')
                city = input('Enter the city you want to see the weather for. Needs to be accurate in spelling: ').lower().capitalize()
                if city == 'q' or city == 'quit':
                    print('You have left the program!\n')
                    exit()
                lineAmount = len(userInput.splitlines())
                deleteLastLine(lineAmount)
                forcastDay, forcastHour, forcastCurrent = asyncio.run(getWeather(city))
                hForcast, fForcast, cForcast = dataFormating(forcastDay, forcastHour, forcastCurrent)
                cForcastConv, fForcastConv, hForcastConv, forcastCurrentCel, forcastDayCel, forcastHourCel = feh2cel(forcastDay, forcastHour, forcastCurrent)
                print('\nHere is your data:\n\nTemps in fahrenheit\n{}\n{}\n{}\nTemps in celsius:\n{}\n{}\n{}\n'.format(cForcast, fForcast, hForcast, cForcastConv, fForcastConv, hForcastConv))

                forcastDataList = [forcastDay, forcastHour, forcastCurrent, forcastDayCel, forcastHourCel, forcastCurrentCel]
                userInput = input('(Y/N) Do you wish to convert this data to a excel file?\n').lower()
                lineAmount = len(userInput.splitlines()) - 1
                deleteLastLine(lineAmount)
                if userInput == 'y':
                    excelConv(forcastDataList)
                elif userInput == 'n':
                    # New condition to print objects to terminal! 
                    # print('\nHere is your data:\n\nTemps in fahrenheit\n{}\n{}\n{}\nTemps in celsius:\n{}\n{}\n{}\n\The data here is represetned in strings.'.format(cForcast, fForcast, hForcast, cForcastConv, fForcastConv, hForcastConv))
                    print(f'\nHere is your data:\n\nTemps in fahrenheit\n{cForcast}\n{fForcast}\n{hForcast}\nTemps in celsius:\n{cForcastConv}\n{fForcastConv}\n{hForcastConv}\n\The data here is represetned in strings.')
                    break
                elif userInput == 'q':
                    print('You have quit the program!\n')
                    exit()
                else:
                    print('User input is not supported: "{}"'.format(userInput))
                    exit()
                    
                userInput = input('(Y/N) Do you want this information sent to your email?: ').lower()
                lineAmount = len(userInput.splitlines()) - 1
                deleteLastLine(lineAmount)
                if userInput == 'y':
                    body = sendMail(hForcast, fForcast, cForcast, cForcastConv, fForcastConv, hForcastConv)
                elif userInput == 'n':
                    print('Continuing on!\n\n')
                elif userInput == 'q':
                    print('You have quit the program!\n')
                    exit()
                else:
                    print('User input is not supported: "{}"'.format(userInput))
                    exit()
                    
    elif userInput == 'n' or userInput == 'q':
        print('You have quit the program.\n')
    else:
        print('You have entered a incorrect value: {}\nQuiting the program...'.format(userStart))
        exit()
