# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:57:04 2022

@author: 박상일
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('2020-01-01', periods=48, freq='M')
dates

# additive model: trend + cycle + seasonality + irregular factor


timestamp = np.arange(len(dates))
trend_factor = timestamp*1.1
cycle_factor = 10*np.sin(np.linspace(0, 3.14*2, 48))
seasonal_factor = 7*np.sin(np.linspace(0, 3.14*8, 48))
np.random.seed(2004)
irregular_factor = 2*np.random.randn(len(dates))


df = pd.DataFrame({'timeseries': trend_factor + cycle_factor + seasonal_factor + irregular_factor, 
                   'trend': trend_factor, 
                   'cycle': cycle_factor, 
                   'trend_cycle': trend_factor + cycle_factor,
                   'seasonal': seasonal_factor, 
                   'irregular': irregular_factor},
                   index=dates)


df