### Pandas `resample` vs. `asfreq` in Time Series

In time series analysis with Pandas, both `resample` and `asfreq` are used for frequency conversion, but they serve different purposes:

#### `resample`
- **Purpose**: Aggregates data over a new time frequency, typically used for downsampling or upsampling time series data.
- **How it Works**: Resampling changes the frequency of the time series by applying a function (like `mean`, `sum`, etc.) to group the data into the new frequency.
- **Example**: Resampling hourly data to daily data by calculating the daily average.
  ```python
  df.resample('D').mean()
  ```
- **Use Case**: When you need to compute statistics (e.g., mean, sum, etc.) over a new time period.

#### `asfreq`
- **Purpose**: Changes the frequency of the time series without any aggregation, just changes the frequency and fills missing periods with `NaN` or a specified method.
- **How it Works**: Simply alters the frequency of the data and keeps the original values intact, inserting `NaN` for missing values if the new frequency is higher.
- **Example**: Converting daily data to hourly data without aggregation.
  ```python
  df.asfreq('H')
  ```
- **Use Case**: When you need to create a regular time series without aggregation, such as filling in missing time steps or expanding data to a higher frequency.

#### Comparison with Time Series
- **Resample**: Suitable for time series operations where you need to change the frequency and also summarize the data over time periods.
- **Asfreq**: Ideal for maintaining original data points when changing frequency, commonly used to align data to a new time interval.

Both methods are essential for handling time series data, but the choice between them depends on whether you need to aggregate data or just adjust its frequency while retaining original values.


## Resources
1. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html
2. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html
