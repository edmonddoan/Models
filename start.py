import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

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

signals['signal'] = np.where(signals['short_mavg'] > signals['long_mavg'], 1.0, 0.0)

signals['positions'] = signals['signal'].diff()

print(signals[signals['positions'] !=0].head())

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111, ylabel=f'{ticker} Price in $')

signals['price'].plot(ax=ax1, color='gray', lw=1.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

plt.title('Simple Moving Average Strategy')
plt.legend()
plt.show()