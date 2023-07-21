import csv
import os
import pandas as pd
from datetime import date

def excelConv(forcastDataList):
    currentDate = date.today().strftime('%Y-%m-%d')
    outputDir = '~/Downloads/'
    os.makedirs(outputDir, exist_ok=True)     # Create the output directory if it doesn't exist

    for data in forcastDataList:
        filename = f'weatherData_{data}.xlsx'
        outputFile = os.path.join(outputDir, filename)

        if not os.path.exists(outputFile):
            # Create a new Excel file and add the data
            df = pd.DataFrame(data)
            df.to_excel(outputFile, sheet_name=currentDate, index=False)
            print(f'The data for {data} has been saved to a new Excel file: {outputFile}\n')
        else:
            # Append the data to an existing Excel file
            with pd.ExcelWriter(outputFile, mode='a', engine='openpyxl') as writer:
                df = pd.DataFrame(data)
                df.to_excel(writer, sheet_name=currentDate, index=False)
                print(f'The data for {data} has been saved to existing Excel file: {outputFile}\n')
    print('All data has been created sucsfully!\n')

    return