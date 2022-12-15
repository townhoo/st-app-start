import pandas as pd
from pandas.io.json import json_normalize
import json
import requests
import numpy as np
import matplotlib.pyplot as plt


def get_api_result(url):
  r = requests.get(url)
  return json.loads(r.text)


def get_exchange_rate(start_dt=None, end_dt=None, symbols=['THB','JPY'], base_currency='USD'):
  if start_dt is None:
    start_dt = (pd.Timestamp.now() - pd.DateOffset(days=15)).strftime('%Y-%m-%d')
  if end_dt is None:
    end_dt = pd.Timestamp.now().strftime('%Y-%m-%d')
  url = f'https://api.exchangerate.host/timeseries?start_date={start_dt}&end_date={end_dt}&base={base_currency}&symbols={",".join(symbols)}'
  print(url)
  r=requests.get(url)
  j=json.loads(r.text)
  df=pd.DataFrame(j['rates']).T
  df.sort_index(inplace=True)
  return df

def get_forex_rate(pairs='EURUSD'):
  url = f'https://www.freeforexapi.com/api/live?pairs={",".join(pairs)}'
  print(url)
  r=requests.get(url)
  j=json.loads(r.text)
  df=pd.DataFrame(j['rates']).T
  df.sort_index(inplace=True)
  return df
