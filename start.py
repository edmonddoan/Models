import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-12-31'

data = yf.download(ticker, start=start_date, end=end_date)

print(data.head())

short_window = 50
long_window = 200

# Create a new Dataframe to store our signals and data
signals = pd.DataFrame(index=data.index)
signals['price'] = data['Close']

signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

print(signals.head())

