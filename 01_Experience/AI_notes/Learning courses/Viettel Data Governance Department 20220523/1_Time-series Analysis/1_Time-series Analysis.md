# Time-series
## Definition
- Time-series is an ordered sequence of values that are usually equally spaced over time
- The univariate time series consists of a single observation (target)
- The multivariate time series consists of more than one observations

## Characteristics
- The sequence of the observations is important
- Time-series data typically possess dependence patterns (components) between observations
- This dependency can be use to produce low-variance forecasts

## Components
- 4 behaviors:
	- Trend component:
		- Overall, persistent long-term upward or downward movement
		- Trend can be linear or non-linear
	- Cyclical component:
		- Repeating swings or movements over more than one year
		- The cycles **do not have a fixed frequency**
		- It is often measured peak to peak or trough to trough.
	- Seasonal component:
		- Regular periodic fluctuation, usually within a 12- month period
		- It **has a fixed and known frequency**
	- Irregular component:
		- Erratic or residual fluctuations
		- They are unpredictable and can be thought of as random errors
		- Their causes are random variations of nature, accidents, unusual events, noise

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Components.png]]

## Time-series components analysis
- Additive
- Multiplicative

# Moving averages
## Definition
- We use moving averages to smooth large irregular component to achieve a clearer picture of visual interpretation
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Moving averages.png]]

## Types of windows in moving averages
- Centered moving average: (for smoothing)
	- Window centered around time t: $$\frac{x_{average} = x_{t-1} + x_t + x_{t+1}}{3}$$

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Centered moving average.png]]

- Trailing Moving Average: (for predicting)
	- Window from time t and backwards: $$\frac{x_{average} = x_{t-2} + x_{t-1} + x_t}{3}$$
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Trailing Moving Average.png]]

## Order of Moving Averages
- Order of Moving Averages = the size of windows (the number of value in each window)

## Weighted Moving Averages

## Moving Averages of Moving Averages
- It aims to make an even-order moving average symmetric

## Moving Averages for Time-series Decomposition
- We can use Moving Averages to remove seasonal components and identify trend and/or cyclical components

## Moving Averages for Time-series Forecasting
- Not a good forecast technique
- It is mainly used to get an overall trend
- Mainly use as baseline for other techniques
- Disadvantages:
	- Seasonal fluctuations are suppressed
	- Lag behind in terms of trend due to usage of the most recent values


# Exponential Smoothing
## Definition
- Forecasts produced using exponential smoothing methods are **weighted averages** of past observations
- The weights decays exponentially as the observations get older

- **Types of Exponential Smoothing**:
	- Simple Exponential Smoothing:
		- For series with no trend or seasonality
	- Holt’s Exponential Smoothing
		- For series with trend and no seasonality
	- Holt-Winter's Exponential Smoothing
		- For series with trend and seasonality


## Simple Exponential Smoothing
- For series with no trend or seasonality

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Simple Exponential Smoothing.png]]
$${
\begin{align}
F_{t+1} &= \alpha y_t + \alpha (1- \alpha) y_{t-1} + \alpha (1- \alpha)^2 y_{t-2} + ...\\
&= \alpha y_t + (1- \alpha)(\alpha y_{t-1} + \alpha (1- \alpha) y_{t-2}) + ...\\
&= \alpha y_t + (1- \alpha) F_t\\
&= F_t + \alpha (y_t-F_t)\\
&= F_t + \alpha e_t\\

\end{align}
}$$
-  The forecast is mainly calculated using: $$F_{t+1} = F_t + \alpha e_t$$
	- $α$ is a constant between 0 and 1, called the smoothing constant
	- $e_t$ is the forecast error at time t: $e_t = y_t - F_t$
	- F is the forecast
	- y is the real value


## Choosing Smoothing Constant α
- The smoothing constant α determines the learning rate and weight of past value. 
	- α close to 1,  past values have no influence over forecasts (under-smoothing)
	- α close to 0,  past values have equal influence over forecasts (over-smoothing)
	- Rule of thumb: $\alpha \in [0.1, 0.2]$
	- Find the best smoothing constant while minimizing predictive accuracy (MAPE, RMSE,…)

## Holt’s Exponential Smoothing
- For series with trend and no seasonality

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Holt’s Exponential Smoothing.png]]

## Holt-Winter’s Exponential Smoothing
- For series with trend and seasonality

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Winter’s Exponential Smoothing.png]]

- M is one season time 
	- M=12 for monthly data
	- M=4 for quarterly data

## Comparing
- Moving average, and simple exponential smoothing yield a constant forecasting value as they do not consider trend nor seasonality.
- Holt's method produces increasing or decreasing forecasts as only considering trend.
- Only Holt-Winter's generates forecasts that incorporate both trend and seasonality and performs best on this task.

---
> Not understand much after this line
# Regression-based Models
## Definition
- Regression can be used to find **global trend** of the entire series in the forecasting period
- Linear trend: a fixed amount increase/ decrease
- Exponential trend: multiplicative increase/ decrease
- Polynomial trend: quadratic relationship between predictors and target variable

## Regression-based Model capturing Seasonality

# Auto-regression Models
## Autocorrelation and Measuring Autocorrelation
- Autocorrelation (or serial correlation) is correlation patterns existing between values in adjacent periods in the series (pairs of values at a certain lag)
- Finding big fluctuation in a certain lag
	- E.g. Every 6 month, price reduce greatly -> Autocorrelation lag-6 is significant (big number)


## Autocorrelation function vs Partial Autocorrelation function
- ?

## Autoregressive Model
- ?
## Autoregressive Integrated Moving Average Model
- ?
- Using to remove trend and seasonal


---
> Practical classes
# Classical approaches
## Pros
- Rather easy to use and to implement yourself 
- Are present out of the box in many packages (often - with auto-tuning functionality)
- Shines for short or unrelated time-series and known state of world
- Good theoretical base -> every econometrician knows them better than his/her own girl/boy friend :)
- Easier to explore and to interpret than complicated ML models

## Cons
- Fail when the historical data available is limited
- Not optimal when there are many distinct, but related, time series (dependent assortment, different stores)
- There are many high cardinality categorical variables (stores, SKUs, brands, etc.)
- Require strong assumptions (stationarity, etc.)
- Require frequent retraining
- Fail at inference time if new time series arises


# Regression Approaches
- Time axis is encoded via features (month, weekday, hour, etc.) 
- Autocorrelation is encoded via lags and its derivatives
- Those features are joined with other features: categorical encodings, numeric features, other heterogenous data 
- Assumptions are relaxed a bit
- Greater flexibility arises (from linear regression to deep neural networks)


# Validation Strategy

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Validation Strategy.png]]


# Feature types
## Source classification
| Type        | Subtype           | Examples                                                  | Transformation                   |
| ----------- | ----------------- | --------------------------------------------------------- | -------------------------------- |
| Categorical | known cardinality | Weekday, week number, month.                              | One-hot-encoding, Label encoding |
|             | temporal          | Store, brand, category, region                            | Hashing + One-hot-encoding       |
| Numeric     | magnitude-bounded | Price diff, sales diff                                    | Identity                         |
|             | unbounded/skewed  | Price, visitors count, stocks, temperature, currency rate | Standard Scale, MinMax Scale     |
| Text        | direct embedding  | Product description, reviews                              | W2V, GloVe, FastText, etc.       |
| Picture     | direct embedding  | Product image                                             | Embeddings from pre-trained CNNs | 

## Temporal classification

| Type       | Examples                                                                               |
| ---------- | -------------------------------------------------------------------------------------- |
| Static     | Product text description, Category, Brand                                              |
| Historical | Visitors count, Sales, Price, Promo, Popularity, Discount, Weather, Competitors prices |
| Future     | Price, Discount, Promo, Holidays                                                                                       |

# Simple Dense Neural Network
- Each feature has no relationship with others
- Pros: 
	- Simple implementation 
	- Doesn’t require specific data transformation before training - works with tabular data out of the box 
	- Fast training and inference (even on CPU) 
	- Requires less data to train on
- Cons: 
	- Need to select and add lags for dynamic features manually to mimic temporal dependencies 
	- Complicated chained inference for prediction on several steps ahead: Requires explicit recalculation of future dataset at inference time
	- Harder to catch implicit temporal dependencies

# CNN Approach

## Fully connected
- Fully connected:
	- Units in hidden layer are connected to every unit in previous layer
- Convolution layer: 
	- Units in hidden layer operate on a field of the input
	- Weights are shared across input






















# 

---
- Status: #done

- Tags: #time_series

- References:
	- 

- Related:
	- 
