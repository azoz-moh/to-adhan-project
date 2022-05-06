from fastapi import FastAPI
import pandas as pd
from datetime import datetime
import json
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

x122 = 11
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Machine_date = datetime.today().strftime('%d-%m')


@app.get('/')
def to_pray():
    df = pd.read_excel('Salah-Calendar.xlsx', sheet_name='Table 1', usecols="A:L")
    for row in range(len(df)):
        if df.loc[row]['Date'].strftime('%d-%m') == Machine_date:
            adan = {
                "Date": df.loc[row]['Date'].strftime('%m-%d'),
                "Fajr": df.loc[row]['Fajr'],
                "Fajr_Iqama": df.loc[row]['Fajr Iqama'].strftime('%H:%M'),
                "Sunrise": df.loc[row]['Sunrise'],
                "Zuhr": df.loc[row]['Zuhr'],
                "Zuhr_Iqama": df.loc[row]['Zuhr Iqama'].strftime('%I:%M'),
                "Asr": df.loc[row]['Asr'],
                "Asr_Iqama": df.loc[row]['Asr Iqama'].strftime('%I:%M'),
                "Maghrib": df.loc[row]['Maghrib'],
                "Maghrib_Iqama": df.loc[row]['Maghrib Iqama'].strftime('%H:%M'),
                "Isha": df.loc[row]['Isha'],
                "Isha_Iqama": df.loc[row]['Isha Iqama'],
            }
            
            return JSONResponse(content=adan)
        # END
