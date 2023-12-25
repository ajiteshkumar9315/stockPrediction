# fBuBzN4_yt6LRnZX9Ry1 this is  api key of quandl

import pandas as pd
import quandl as qd
import numpy as np
import matplotlib.pyplot as plt

# plt as plot

print('hello world')

qd.ApiConfig.api_key = "fBuBzN4_yt6LRnZX9Ry1"
msft_data = qd.get("EOD/MSFT", start_date="2010-01-01", end_date="2020-01-01")

msft_data.head()

close_price = msft_data[['Adj_Close']]

daily_return = close_price.pct_change()

daily_return.fillna(0, inplace=True)

print(daily_return)

adj_prince = msft_data['Adj_Close']

mav = adj_prince.rollong(window=50).mean()

print(mav[-10:])

adj_prince.plot()

mav.plot()
