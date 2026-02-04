# Gold-price-prediction
This project investigates the long-term economic trajectory of gold prices in the Indian market. Gold is not merely a commodity in India. It serves as a primary vehicle for savings and a hedge against the devaluation of the Rupee. By analyzing data spanning 100 years at 10-year intervals, the study aims to filter out minor market fluctuations to reveal the underlying growth trend.
DATASET DESCRIPTION:
The dataset is composed of 11 distinct observations, meticulously recorded at ten-year intervals. This deliberate decadal approach serves a specific purpose: it emphasizes the profound "compounding" effects of economic shifts over time, rather than the fleeting fluctuations observed in daily trading. This method allows for a clearer understanding of how trends and patterns evolve, showcasing the cumulative impact of economic changes across a broader temporal landscape.
Methodology: ARIMA (1,1,1)
•	The analysis utilises the ARIMA model, which stands for Autoregressive Integrated Moving Average, specifically configured as (1,1,1). This powerful statistical tool is particularly adept at handling non-stationary data—data that exhibits shifting patterns in mean and variance over time, a phenomenon often observed in volatile economic markets.
•	Trend Identification: The ARIMA model excels in recognising underlying trends within time series data, making it a vital choice for analysing patterns that evolve.
•	Autoregression (1): At its core, the model leverages the relationship between a current observation and its past values, thus capturing the inertia in data. This autoregressive component is crucial for understanding how past behaviours influence present outcomes.
•	Integration (1): To convert non-stationary data into a stationary format, ARIMA employs a technique known as "differencing." This method highlights the rate of change rather than the actual values, allowing the model to zero in on the dynamics of the data.
•	Moving Average (1): The model further incorporates a moving average component, which accounts for the correlation between an observation and the residual errors from previous predictions. This aspect enhances the model’s predictive power by correcting for past inaccuracies.
•	In sum, the ARIMA (1,1,1) configuration provides a robust framework for analysing complex time series data, enabling effective forecasting in unpredictable environments.
The trained ARIMA model forecasts a continued, aggressive upward surge in value. For the year 2036, the predicted gold price is:
₹ 3,21,722.22 per 10 grams.
