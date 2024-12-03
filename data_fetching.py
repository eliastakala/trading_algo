# import yfinance as yf
# import pandas as pd

# # Define the stock symbol and the date range
# ticker = "TSLA"
# start_date = "2020-01-01"  # 3 years from today
# end_date = "2023-12-31"

# # Fetch historical daily data for the specified range
# data = yf.download(ticker, start=start_date, end=end_date, interval='1d')

# # Display the first few rows of the data
# print(data.columns)
# data['Price']
# # Save the data to a CSV file for later use
# data.to_csv("trading_algo/tesla_daily_data.csv")

import yfinance as yf
import pandas as pd

# Download Tesla stock data
ticker = "TSLA"
start_date = "2020-01-01"
end_date = "2023-12-31"
df = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Flatten MultiIndex columns
df.columns = [' '.join(col).strip() for col in df.columns.values]

print(df.head())
# Save to CSV
df.to_csv("trading_algo/tesla_flattened_data.csv", index=True)
print("Data saved to tesla_flattened_data.csv")
