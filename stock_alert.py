import pandas as pd
from alpha_vantage.timeseries import TimeSeries 

import matplotlib.pyplot as plt

import time 

import smtplib

#to get data from alpha_vantage, format as pandas df
ts = TimeSeries(key='US6OEWG84TYP1JAD', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='VERU', interval='1min', outputsize='full')

close_data = data['4. close']
last_price = close_data[0]
price_yest = close_data[1]
high_price = data['2. high']
last_high = high_price[0]
print(last_price)
print(price_yest)
print(last_high)


