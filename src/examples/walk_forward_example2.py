from pandas import read_csv
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd

from math import sqrt
# load data
series = read_csv('../../datasets/example_datasets/dataset.csv', header=0)
series["Month"] = pd.to_datetime(series["Month"])
series = series.set_index('Month')

X = series.values
X = X.astype('float32')

train_size = int(len(X) * 0.50)
train, test = X[0:train_size], X[train_size:]
# walk-forward validation
history = [x for x in train[1:]]
predictions = list()
for i in range(len(test)):
	# predict
    model = ARIMA(history, order=(0,1,2))
    model_fit = model.fit(disp=0)
    yhat = model_fit.forecast()[0]
    predictions.append(yhat)
    # observation
    obs = test[i]
    history.append(obs)
    print('>Predicted=%.3f, Expected=%3.f' % (yhat, obs))
# report performance
mse = mean_squared_error(test, predictions)
rmse = sqrt(mse)
print('RMSE: %.3f' % rmse)
test_series = pd.Series(test.flatten(), index=series[train_size:].index)
prediction_series = pd.Series(predictions, index=series[train_size:].index)
plt.figure(figsize=(6,4))

plt.plot(series, label="original")
plt.plot(test_series, label="test", color="black")
# plt.plot(series, label="train")
plt.plot(prediction_series, color="red", label="predictions")
plt.show()