# TRY Plotly
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from tabulate import tabulate

def daily_forecast_plot(daily_forecast):
        fig = go.figure()
        fig.add_trace(go.Bar(x=daily_forecast['forcastDate'], y=daily_forecast['highTemp'], name='High Temp'))
        fig.add_trace(go.Bar(x=daily_forecast['forcastDate'], y=daily_forecast['lowTemp'], name='Low Temp'))
        
        fig.update_layout(title='Daily Temperature Forecast',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Temperature (°F)'),
                      barmode='group')
        
        return fig


def plot_forcast_data(forcastDataList):
        for forcast_data in forcastDataList:
                if 'forcastDay' in forcast_data:
                        fig = daily_forecast_plot(forcast_data)
                        print('DEBUG PRINT')
                        fig.show()
                else:
                        continue
        
        print(forcastDataList)
        print(type(forcastDataList))

        for forecast_data in forcastDataList:
                print("Forecast Data:")
                print(forecast_data)
                print("\n" + "=" * 30 + "\n")  # Separator for better readability

        return
    