import pandas as pd
import yfinance as yf
price_history = yf.Ticker('TSLA').history(period='ytd', interval='1d', actions=False)
price_history
#valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#action=False drops empty coulumns
