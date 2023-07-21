import os
import csv
import pandas as pd
from datetime import date

forcastHour = {
    'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
    'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
    'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
}

def excelConv(forcastHour):
    currentDate = date.today().strftime('%Y-%m-%d')
    outputDir = '/Users/hunterpimparatana/Documents/'
    outputFile = os.path.join(outputDir, 'outputWeatherData.xlsx')
   
    # Create the output directory if it doesn't exist
    os.makedirs(outputDir, exist_ok=True)

    if not os.path.exists(outputFile):
        # Create a new Excel file and add the data
        df = pd.DataFrame(forcastHour)
        df.to_excel(outputFile, sheet_name=currentDate, index=False)
        print(f'The data has been saved to a new Excel file: {outputFile}')
    else:
        # Append the data to an existing Excel file
        with pd.ExcelWriter(outputFile, mode='a', engine='openpyxl') as writer:
            df = pd.DataFrame(forcastHour)
            df.to_excel(writer, sheet_name=currentDate, index=False)
            print(f'The data has been added to the existing Excel file: {outputFile}')

    return

excelConv(forcastHour)
