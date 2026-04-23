import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

start = dt.datetime(2026, 1, 1)
end = dt.datetime.now()

data = yf.download("AAPL", start=start, end=end)
data = data[['Open', 'High', 'Low', 'Close']].dropna()

data.reset_index(inplace=True)

# Convert dates
data['Date'] = mdates.date2num(data['Date'])

# Ensure correct column order
ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']]

fig, ax = plt.subplots()

# Styling
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.tick_params(colors='white')
ax.grid(True)

# Format dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis_date()

# Plot candlesticks
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

