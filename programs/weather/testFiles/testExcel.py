import os
import csv
import pandas
from datetime import date

def excelConv(forcastHour):
    currentDate = date.today().strftime('%Y-%m-%d')
    outputFile = os.path.expanduser('~/Downloads/output.csv')

    with pd.ExcelWriter(outputFile, mode='a', engine='openpyxl') as writer:
            df = pd.DataFrame(forcastHour)
            df.to_excel(writer, sheet_name=currentDate, index=False)

    return


forcastHour = {
    'forcastHour': ['12:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM'],
    'temperature': ['88', '86', '89', '90', '88', '92', '84', '81'],
    'description': ['Clear', 'Clear', 'Sunny', 'Sunny', 'Sunny', 'Clear', 'Sunny', 'clear']
}

excelConv(forcastHour)

