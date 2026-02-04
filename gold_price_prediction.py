import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("india_gold_100_years_10yr_interval.csv")

print(df)

# -----------------------------------------
# 2. Visualize Historical Gold Prices
# -----------------------------------------
plt.figure()
plt.plot(df["Year"], df["Price_INR_per_10g"], marker='o')
plt.title("India Gold Prices (1926–2025)")
plt.xlabel("Year")
plt.ylabel("Gold Price (INR per 10g)")
plt.grid(True)
plt.savefig('historical_prices.png')

# -----------------------------------------
# 3. Prepare Time Series Data
# -----------------------------------------
gold_series = df["Price_INR_per_10g"]

# -----------------------------------------
# 4. Train ARIMA Model
# -----------------------------------------
# ARIMA(p,d,q) → (1,1,1) works well for trend-based data
model = ARIMA(gold_series, order=(1, 1, 1))
model_fit = model.fit()

# -----------------------------------------
# 5. Forecast Gold Price for 2036
# -----------------------------------------
# One step ahead ≈ next 10-year interval (2036)
forecast = model_fit.forecast(steps=1)
predicted_price_2036 = round(float(forecast.iloc[0]), 2)
print("Predicted Gold Price for India in 2036:")
print(f"₹ {predicted_price_2036} per 10 grams")

# -----------------------------------------
# 6. Plot Forecast
# -----------------------------------------
years_extended = df["Year"].tolist() + [2036]
prices_extended = df["Price_INR_per_10g"].tolist() + [predicted_price_2036]

plt.figure()
plt.plot(years_extended[:-1], prices_extended[:-1], label="Historical Data", marker='o')
plt.plot(years_extended[-2:], prices_extended[-2:], 
         label="Forecast (2036)", marker='o', linestyle='--')

plt.title("India Gold Price Forecast up to 2036")
plt.xlabel("Year")
plt.ylabel("Gold Price (INR per 10g)")
plt.legend()
plt.grid(True)
plt.savefig('forecast.png')