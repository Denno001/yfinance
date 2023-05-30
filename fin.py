#..volaitity is the price movement of a stock this can be thought as the equivalent of the risk of the stock
#..volatility can also be viwed as te return of the stock
#..we can use average true range(ATR) to calculate volatility
#formula
#..TR=max[H-l,|H-Cp,|L-Cp|]
#..ATR=1/n summation)n/i=1 TRiTR = max[H-L,| H-Cp|, |L-Cp|]
#ATR =1/n ∑_(i=1)^n▒TRi

#..TR = a particuar true range
#..n=time period, H=current high, L=current low, Cp=previous close

import pandas as pd
import numpy as np
import yfinance as yf

data = yf.download("AMZN", start="2022-01-01", end="2022-12-31")
data

#..break the fomula down H-L
high_low = data['High']-data['Low']
high_low

#..H-Cp np.abs is for absolute values i.e it drops negative values
high_cp = np.abs(data['High']-data['Close'].shift())
high_cp

low_cp = np.abs(data['Low']-data['Close'].shift())
high_cp

#..creating a maxima
df = pd.concat([high_low, high_cp, low_cp], axis=1)
df

true_range = np.max(df, axis=1)
true_range

#basically getting the mean of true range using n which is number of entries in this case 251
average_true_range = true_range.rolling(251).mean()
average_true_range

#..visualizing ATR
import matplotlib.pyplot as plt
%matplotlib notebook
fig, ax = plt. subplots()
average_true_range.plot(ax=ax)
ax2 = data['Close'].plot(ax=ax, secondary_y=True,)
ax.set_ylabel('ATR')
ax2.set_ylabel('Price')
#..secondary y = true makes both lines to use same scale you can add alpha=.3 if lines not transparent
