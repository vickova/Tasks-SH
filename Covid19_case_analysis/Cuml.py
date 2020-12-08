import pandas as pd
import datetime
import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.dates as md
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Clean the time series
df = pd.read_csv('CumulativeCases.csv')
df = pd.DataFrame(df).fillna('Nil')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 2. Calculate the measures of central tendencies of your time series
df1 = df[['Belgium', 'Colombia']]
data = df1.copy()
data = data.reset_index().drop('Date', axis=1)
print(data)

xls = df1.describe()
xls.to_excel('Disperse.xlsx')

df = df.reset_index()

# 3. The frequencies of your time series
print('Frequency of the time series per day')
df1_freq_daily = df1.asfreq('D')
print('Frequency of the time series per week')
df1_freq_weekly = df1.asfreq('W')
print('Frequency of the time series per month')
df1_freq_monthly = df1.asfreq('Y')
print(df1_freq_daily)
print(df1_freq_weekly)
print(df1_freq_monthly)

# 4. Showing a histogram plot & 5. Customizing the histogram
plt.hist(df1['Colombia'], color='blue', bins=15, alpha=0.5, label='Colombia')
plt.hist(df1['Belgium'], color='red', bins=15, alpha=0.5, label='Belgium')
plt.legend()
plt.ylabel('Frequency')
plt.xlabel('Values')
plt.title('relationship btw the rate of increase of COVID-19 in Colombia and Belgium')
plt.show()
plt.savefig('Histogram.png')

# for mean window
df1_meancol = df1['Colombia'].rolling(window=7).mean(ddof=0)
df1_meanBel = df1['Belgium'].rolling(window=7).mean(ddof=0)

# 6. Choose best window size to calculate teh average
plt.plot(df1_meancol, color='blue', alpha=0.5, label='Colombia')
plt.plot(df1_meanBel, color='red', alpha=0.5, label='Belgium')
plt.legend()
plt.ylabel('Values')
plt.xlabel('Dates')
plt.title('mean of the two time series')
plt.show()
plt.savefig('mean_window.png')

# 7. For Volatility
df1_windcol = df1['Colombia'].rolling(window=2).std(ddof=0)
df1_windBel = df1['Belgium'].rolling(window=2).std(ddof=0)

plt.plot(df1_windcol, color='blue', label='Colombia')
plt.plot(df1_windBel, color='red', label='Belgium')
plt.legend()
plt.ylabel('Values')
plt.xlabel('Dates')
plt.title('Volatility of the two time series')
plt.savefig('Volatility.png')

# 8. write the average anf volatility time series to the csv file
df1['mean_Colomb'] = df1_meancol
df1['mean_Belg'] = df1_meanBel
df1['Volat_Colomb'] = df1_windcol
df1['Volat_Belg'] = df1_windBel
df1.fillna('Nil').to_csv('volat.csv')
print(df1)

# 9. Regression ananlysis
stack = sns.regplot('Colombia', 'Belgium', data, color='blue', label='p').get_figure()
stack.show()
stack.savefig('mine.png')