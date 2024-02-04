import python_weather
import asyncio
import os
import sys, signal
import pandas as pd
sys.path.append('..')
from datetime import datetime
from termios import tcflush, TCIFLUSH
from functions.dataCompile  import dataFormating
from functions.excelConv    import excelConv
from functions.feh2celConv  import feh2cel
from functions.lineRemove   import deleteLastLine
from functions.progressBar  import loadBar
from functions.sendEmail    import sendMail
from functions.weatherData  import getWeather
from functions.locationData import get_location_ip
from functions.graphicRep   import plot_forcast_data

introText = '\n---- Welcome to my Weather Program! ----\n\n----How to use----\n'\
    'Step 1: Enter the city in which you want to see the weather in.\n'\
    'Step 2: Convert the tempatures into celsius if you want to see both displayed.\n'\
    'Step 3: Select to see if you want to information to display on your terminal or sent as email to yourself. (AKA ME AS OF NOW)\n'\
    '\n---- Current issues/upcoming features ----\n'\
    '\n---- This program will also tell you that if its good  ot leave the house! ----\n'\
    'Add to where you can enter the cities name\nCreate unit test to for my program to better run testing. (Create random values for the lists/dictionaries)\n'\
    'Have program automatically know where you are.\n'\

print(introText)

while True:
        try:
            userInput = input('Are you ready to start? (Y/N)\n').lower().strip()
            lineAmount = len(userInput.splitlines() + introText.splitlines())
            deleteLastLine(lineAmount)
            if userInput == 'y':
                location_data = get_location_ip()
                for key, value in location_data.items():
                    if key == 'city':
                        city = value
                        lineAmount = len(userInput.splitlines())
                        deleteLastLine(lineAmount)
                        forcastDay, forcastHour, forcastCurrent = asyncio.run(getWeather(city))
                        hForcast, fForcast, cForcast = dataFormating(forcastDay, forcastHour, forcastCurrent)
                        cForcastConv, fForcastConv, hForcastConv, forcastCurrentCel, forcastDayCel, forcastHourCel = feh2cel(forcastDay, forcastHour, forcastCurrent)
                        print(f'\nHere is your data for {city}:\n\nTemps in fahrenheit\n{cForcast}\n{fForcast}\n{hForcast}\nTemps in celsius:\n{cForcastConv}\n{fForcastConv}\n{hForcastConv}\n')

                        forcastDataList = [forcastDay, forcastHour, forcastCurrent, forcastDayCel, forcastHourCel, forcastCurrentCel]
                        
                        userInput = input('(Y/N) Do you want this information seen in a graph?: ').lower()
                        lineAmount = len(userInput.splitlines()) - 1
                        deleteLastLine(lineAmount)
                        if userInput == 'y':
                            # Does not work due to modules on local device being a silly boi.
                            plot_forcast_data(forcastDataList)
                        elif userInput == 'n':
                            print('Continuing on!\n\n')
                        elif userInput == 'q':
                            print('You have quit the program!\n')
                            exit()
                        else:
                            print('User input is not supported: "{}"'.format(userInput))
                            exit()
                            
                        userInput = input('(Y/N) Do you wish to convert this data to a excel file?\n').lower()
                        lineAmount = len(userInput.splitlines()) - 1
                        deleteLastLine(lineAmount)
                        if userInput == 'y':
                            excelConv(forcastDataList, city)
                        elif userInput == 'n':
                            # New condition to print objects to terminal! 
                            print(f'\nHere is your data:\n\nTemps in fahrenheit\n{cForcast}\n{fForcast}\n{hForcast}\nTemps in celsius:\n{cForcastConv}\n{fForcastConv}\n{hForcastConv}\n')
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
                            
                    elif key == "":
                        print('\nUnable to find location... \nStarting program over!\n')
                        break

            elif userInput == 'n' or userInput == 'q':
                print('You have quit the program.\n')
                exit()
            else:
                print('You have entered a incorrect value: {}\nQuiting the program...'.format(userStart))
                exit()
        except KeyboardInterrupt:
            print('\nProgram has been interrupted: Exiting...\n')
            sys.exit(0)
