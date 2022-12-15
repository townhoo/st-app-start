import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np
from pandas.io.json import json_normalize
import datetime
import json
import requests
import api

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.title('Currency Exchange')
st.write("Hatairat Teeravorawan 6416030473")


st.header('Exchange Rate')
st.markdown('This website is used to view currency. You can compare currency throughout the year. and compare all currencies.')




# THB = 137
# USD = 148
currency = ('AFN',
'ALL',
'AMD',
'ANG',
'AOA',
'ARS',
'AUD',
'AWG',
'AZN',
'BAM',
'BBD',
'BDT',
'BGN',
'BHD',
'BIF',
'BMD',
'BND',
'BOB',
'BRL',
'BSD',
'BTC',
'BTN',
'BWP',
'BYN',
'BZD',
'CAD',
'CDF',
'CHF',
'CLF',
'CLP',
'CNH',
'CNY',
'COP',
'CRC',
'CUC',
'CUP',
'CVE',
'CZK',
'DJF',
'DKK',
'DOP',
'DZD',
'EGP',
'ERN',
'ETB',
'EUR',
'FJD',
'FKP',
'GBP',
'GEL',
'GGP',
'GHS',
'GIP',
'GMD',
'GNF',
'GTQ',
'GYD',
'HKD',
'HNL',
'HRK',
'HTG',
'HUF',
'IDR',
'ILS',
'IMP',
'INR',
'IQD',
'IRR',
'ISK',
'JEP',
'JMD',
'JOD',
'JPY',
'KES',
'KGS',
'KHR',
'KMF',
'KPW',
'KRW',
'KWD',
'KYD',
'KZT',
'LAK',
'LBP',
'LKR',
'LRD',
'LSL',
'LYD',
'MAD',
'MDL',
'MGA',
'MKD',
'MMK',
'MNT',
'MOP',
'MRU',
'MUR',
'MVR',
'MWK',
'MXN',
'MYR',
'MZN',
'NAD',
'NGN',
'NIO',
'NOK',
'NPR',
'NZD',
'OMR',
'PAB',
'PEN',
'PGK',
'PHP',
'PKR',
'PLN',
'PYG',
'QAR',
'RON',
'RSD',
'RUB',
'RWF',
'SAR',
'SBD',
'SCR',
'SDG',
'SEK',
'SGD',
'SHP',
'SLL',
'SOS',
'SRD',
'SSP',
'STD',
'STN',
'SVC',
'SYP',
'SZL',
'THB',
'TJS',
'TMT',
'TND',
'TOP',
'TRY',
'TTD',
'TWD',
'TZS',
'UAH',
'UGX',
'USD',
'UZS',
'VES',
'VND',
'VUV',
'WST',
'XAF',
'XAG',
'XAU',
'XCD',
'XDR',
'XOF',
'XPD',
'XPF',
'XPT',
'YER',
'ZAR',
'ZMW',
'ZWL')

forex = ('AUDUSD',
  'EURGBP',
  'EURUSD',
  'GBPUSD',
  'NZDUSD',
  'USDAED',
  'USDAFN',
  'USDALL',
  'USDAMD',
  'USDANG',
  'USDAOA',
  'USDARS',
  'USDATS',
  'USDAUD',
  'USDAWG',
  'USDAZM',
  'USDAZN',
  'USDBAM',
  'USDBBD',
  'USDBDT',
  'USDBEF',
  'USDBGN',
  'USDBHD',
  'USDBIF',
  'USDBMD',
  'USDBND',
  'USDBOB',
  'USDBRL',
  'USDBSD',
  'USDBTN',
  'USDBWP',
  'USDBYN',
  'USDBYR',
  'USDBZD',
  'USDCAD',
  'USDCDF',
  'USDCHF',
  'USDCLP',
  'USDCNH',
  'USDCNY',
  'USDCOP',
  'USDCRC',
  'USDCUC',
  'USDCUP',
  'USDCVE',
  'USDCYP',
  'USDCZK',
  'USDDEM',
  'USDDJF',
  'USDDKK',
  'USDDOP',
  'USDDZD',
  'USDEEK',
  'USDEGP',
  'USDERN',
  'USDESP',
  'USDETB',
  'USDEUR',
  'USDFIM',
  'USDFJD',
  'USDFKP',
  'USDFRF',
  'USDGBP',
  'USDGEL',
  'USDGGP',
  'USDGHC',
  'USDGHS',
  'USDGIP',
  'USDGMD',
  'USDGNF',
  'USDGRD',
  'USDGTQ',
  'USDGYD',
  'USDHKD',
  'USDHNL',
  'USDHRK',
  'USDHTG',
  'USDHUF',
  'USDIDR',
  'USDIEP',
  'USDILS',
  'USDIMP',
  'USDINR',
  'USDIQD',
  'USDIRR',
  'USDISK',
  'USDITL',
  'USDJEP',
  'USDJMD',
  'USDJOD',
  'USDJPY',
  'USDKES',
  'USDKGS',
  'USDKHR',
  'USDKMF',
  'USDKPW',
  'USDKRW',
  'USDKWD',
  'USDKYD',
  'USDKZT',
  'USDLAK',
  'USDLBP',
  'USDLKR',
  'USDLRD',
  'USDLSL',
  'USDLTL',
  'USDLUF',
  'USDLVL',
  'USDLYD',
  'USDMAD',
  'USDMDL',
  'USDMGA',
  'USDMGF',
  'USDMKD',
  'USDMMK',
  'USDMNT',
  'USDMOP',
  'USDMRO',
  'USDMRU',
  'USDMTL',
  'USDMUR',
  'USDMVR',
  'USDMWK',
  'USDMXN',
  'USDMYR',
  'USDMZM',
  'USDMZN',
  'USDNAD',
  'USDNGN',
  'USDNIO',
  'USDNLG',
  'USDNOK',
  'USDNPR',
  'USDNZD',
  'USDOMR',
  'USDPAB',
  'USDPEN',
  'USDPGK',
  'USDPHP',
  'USDPKR',
  'USDPLN',
  'USDPTE',
  'USDPYG',
  'USDQAR',
  'USDROL',
  'USDRON',
  'USDRSD',
  'USDRUB',
  'USDRWF',
  'USDSAR',
  'USDSBD',
  'USDSCR',
  'USDSDD',
  'USDSDG',
  'USDSEK',
  'USDSGD',
  'USDSHP',
  'USDSIT',
  'USDSKK',
  'USDSLL',
  'USDSOS',
  'USDSPL',
  'USDSRD',
  'USDSRG',
  'USDSTD',
  'USDSTN',
  'USDSVC',
  'USDSYP',
  'USDSZL',
  'USDTHB',
  'USDTJS',
  'USDTMM',
  'USDTMT',
  'USDTND',
  'USDTOP',
  'USDTRL',
  'USDTRY',
  'USDTTD',
  'USDTVD',
  'USDTWD',
  'USDTZS',
  'USDUAH',
  'USDUGX',
  'USDUSD',
  'USDUYU',
  'USDUZS',
  'USDVAL',
  'USDVEB',
  'USDVEF',
  'USDVES',
  'USDVND',
  'USDVUV',
  'USDWST',
  'USDXAF',
  'USDXAG',
  'USDXAU',
  'USDXBT',
  'USDXCD',
  'USDXDR',
  'USDXOF',
  'USDXPD',
  'USDXPF',
  'USDXPT',
  'USDYER',
  'USDZAR',
  'USDZMK',
  'USDZMW',
  'USDZWD')


a1, a2 = st.columns(2)

with a1:
    start_dt = st.date_input("start",
    datetime.date(2022, 1, 1))
  
with a2:
    end_dt = st.date_input("stop")

a3, a4 = st.columns(2)

with a3:
    base_currency = st.selectbox(
    'Currency Base',
    currency,
    index=148)
  
with a4:
    symbols = st.multiselect(
    'Currency Compare',
    currency,
    ['THB', 'JPY'])

  


df = api.get_exchange_rate(start_dt, end_dt, symbols, base_currency)


with st.expander("Raw data", expanded=True):

    st.dataframe(df.T )


# Row b
b1, b2 = st.columns((4,6))

df =  api.get_exchange_rate(start_dt, end_dt, symbols ,base_currency)
for c in df.columns:
    df[f'{c}_pct_chg'] = df[c]/df[c][0]-1

with st.expander("Raw data", expanded=True):
    st.dataframe(df )


with b1:
    st.bar_chart(df)

with b2:
    st.line_chart(df.filter(regex='_pct_chg$'))


forex = st.multiselect(
    'FOREX',
    forex,
    ["EURUSD","EURGBP","GBPUSD","USDJPY","AUDUSD","USDCHF","NZDUSD","USDCAD","USDZAR","USDTHB"])


# Row b
c1, c2, c3 = st.columns((2,4,4))


with c1:
    with st.expander("Raw data", expanded=True):
        df_f =  api.get_forex_rate(forex)
        st.dataframe(df_f.T )

with c2: 
    st.bar_chart(df_f['rate'])

with c3: 

    st.line_chart(df_f['rate'], use_container_width=True)