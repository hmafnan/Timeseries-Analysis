import sys
sys.path.append("../")
import copy
import itertools
import operator

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import TimeSeriesSplit
from math import sqrt

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from pydlm import dlm, trend, seasonality, dynamic, autoReg


from src import helpers
from src import dataset

excel_file = "20160921-analysisofestimatedarrivals.xlsx"
data = dataset.load_excel(excel_file, dir="../../datasets")
data = dataset.load_all_regions(data)

df_italy = data["italy"] # Arrivals to Italy
df_greek_island = data["greek_island"] # Arrivals to Greek Island
df_mainland_greece = data["mainland_greece"] # Arrivals to Mainland greece
df_fyrom = data["fyrom"] # Arrivals to fYRoM
df_serbia = data["serbia"] # Arrivals to Serbia
df_croatia = data["croatia"] # Arrivals to Croatia
df_hungry = data["hungry"] # Arrivals to Hungry
df_slovenia = data["slovenia"] # Arrivals to Slovenia
df_austria = data["austria"] # Arrivals to Austria

df = df_austria # Seriies to test
column_name = df.columns[0]

fill_method = "ffill"
df.fillna(0, inplace=True)
df[df.columns[0]] = df[column_name].replace(to_replace=0, method=fill_method) # Replace 0 in series

model = dlm(df[column_name])
model = model + trend(degree=1, discount=0.72, name='trend component')
model = model + seasonality(period=2, discount=0.99, name='seasonality component')

model.fit()
model.plot()
predictions = list(np.array(model.result.predictedObs).flatten())
r2 = r2_score(df, predictions)
rmse = np.sqrt(model.getMSE())
print('RMSE:', rmse)
print('R2:', r2)