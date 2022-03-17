from fastapi import FastAPI
import pandas as pd
from datetime import datetime
import json
from fastapi.responses import JSONResponse


app = FastAPI()

Machine_date = datetime.today().strftime('%d-%m')


@app.get('/')
def to_pray():
    df = pd.read_excel('Salah-Calendar.xlsx', sheet_name='Table 1', usecols="A:L")
    for row in range(len(df)):
        if df.loc[row]['Date'].strftime('%d-%m') == Machine_date:
            adan = {
                'Date': df.loc[row]['Date'].strftime('%d-%m'),
                'Fajr': df.loc[row]['Fajr'],
                'Fajr Iqama': df.loc[row]['Fajr Iqama'].strftime('%I:%M %p'),
                'Sunrise': df.loc[row]['Sunrise'],
                'Zuhr': df.loc[row]['Zuhr'],
                'Asr': df.loc[row]['Asr'],
                'Maghrib': df.loc[row]['Maghrib'],
                'Isha': df.loc[row]['Isha'],
            }
            
            return JSONResponse(content=adan)
