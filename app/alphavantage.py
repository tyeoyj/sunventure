from typing import get_args
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
import os
import pandas as pd
import requests

API_KEY = os.environ.get("API_KEY_AV", "UT1CVCTWD0LVJP4V")
ts = TimeSeries(key=API_KEY, output_format="pandas")
sp = SectorPerformances(key=API_KEY, output_format="pandas")

def get_latest_EOD_close() -> dict: 
    data, metadata = ts.get_daily("COIN", outputsize="compact")
    data.columns = data.columns.str.replace("[0-9].\s*", "", regex=True)
    latest_date = data.index.max()
    return {"date": latest_date, "close": data.loc[latest_date, "close"]}

def get_latest_CPI():
    url = f"https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey={API_KEY}"
    r = requests.get(url)
    data = pd.DataFrame(r.json()["data"])
    data.set_index("date", inplace=True)
    latest_date = data.index.max()
    return {"date": latest_date, "cpi": data.loc[latest_date, "value"]}
    

if __name__ == "__main__":
    get_latest_CPI()