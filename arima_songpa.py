# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:00:55 2022

@author: 박상일
"""

#%% Law Data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx', encoding='UTF-8')
df = df.drop(df.columns[0], axis=1)
df.columns = ["Data", "Price"]
print(df)

dt = pd.read_excel('tax.xlsx', encoding='UTF-8')
dt = dt.drop(dt.columns[0], axis=1)
dt.columns = ["Data", "Tax"]
print(dt)

plt.figure(figsize=(6,6))
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.plot(range(len(df["Data"])), df["Price"])
plt.savefig('서울_raw data.png')
#%% Trend, Seasonality 확인
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

result = sm.tsa.seasonal_decompose(df['Price'], model='additive', freq=12)
result.observed
fig = plt.figure()
fig = result.plot()
fig.set_size_inches(20,7)

plt.savefig('서울_seasonal_decompose.png')
#%% ACF, PACF
import statsmodels.api as sm
fig = plt.figure(figsize=(6,6))
axl = fig.add_subplot(2,1,2)
fig = sm.graphics.tsa.plot_acf(df["Price"], lags=12, ax=axl)
print(fig)
#fig1 = plt.figure(figsize=(6,6))
#ax1 = fig1.add_subplot(2,1,2)
#fig1 = sm.graphics.tsa.plot_pacf(df["Price"], lags=12, ax=axl)
#print(fig1)
#%% Modeling
from statsmodels.tsa.arima_model import ARIMA
import itertools
from tqdm import tqdm

p = range(0,3)
d = range(1,2)
q = range(0,6)

pdq = list(itertools.product(p,d,q))

aic = []
params = []

with tqdm(total = len(pdq)) as pg:
    for i in pdq:
        pg.update(1)
        try:
            model = ARIMA(df["Price"], order=(i))
            model_fit = model.fit()
            aic.append(round(model_fit.aic, 2))
            params.append((i))
        except:
            continue
optimal = [(params[i],j) for i,j in enumerate(aic) if j == min(aic)]
model_opt = ARIMA(df["Price"], order = optimal[0][0])
model_opt_fit = model_opt.fit()
print(model_opt_fit.summary())

fore = model_fit.forecast(steps=24)
print(fore)
#%%ARIMAX
from statsmodels.tsa.arima_model import ARIMA
import itertools
from tqdm import tqdm

p = range(0,3)
d = range(1,2)
q = range(0,6)

pdq = list(itertools.product(p,d,q))

aic = []
params = []

with tqdm(total = len(pdq)) as pg:
    for i in pdq:
        pg.update(1)
        try:
            model = ARIMA(df["Price"], dt["Tax"], order=(i))
            model_fit = model.fit()
            aic.append(round(model_fit.aic, 2))
            params.append((i))
        except:
            continue
optimal = [(params[i],j) for i,j in enumerate(aic) if j == min(aic)]
model_arimax = ARIMA(df["Price"], exog = dt["Tax"], order=(1,1,2))
result2 = model_arimax.fit()
print(result2.summary())

fore = model_fit.forecast(steps=24)
print(fore)