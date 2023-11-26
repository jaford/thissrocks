import csv
import os
import pandas as pd
from datetime import date

def excelConv(forcastDataList, city):
    currentDate = date.today().strftime('%Y-%m-%d')
    outputDir = '~/Downloads/'
    os.makedirs(outputDir, exist_ok=True)     # Create the output directory if it doesn't exist

    for data in forcastDataList:
        dictName = next(iter(data))
        print(f'Dictionary that I am currenty in --> "{dictName}"\nThe data within current dict:\n{data}')
        filename = f'weatherData_{currentDate}_{city}.xlsx'
        outputFile = os.path.join(outputDir, filename)

        if not os.path.exists(outputFile):
            # Create a new Excel file and add the data
            df = pd.DataFrame(data)
            df.to_excel(outputFile, sheet_name=dictName, index=False)
            print(f'The data for {city} and {dictName} has been saved to a new Excel file: {outputFile}\n')
        else:
            # Append the data to an existing Excel file
            with pd.ExcelWriter(outputFile, mode='a', engine='openpyxl') as writer:
                df = pd.DataFrame(data)
                df.to_excel(writer, sheet_name=dictName, index=False)
                print(f'The data for {city} and {dictName} has been saved to existing Excel file: {outputFile}\n')
                
    print('All data has been created sucsfully!\n')

    return