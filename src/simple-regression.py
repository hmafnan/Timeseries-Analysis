import pandas as pd
import matplotlib.pyplot as plt

from src import dataset
import fbprophet
from sklearn.ensemble.forest import RandomForestRegressor

excel_file = "20160921-analysisofestimatedarrivals.xlsx"


df = dataset.load_excel(excel_file)

# Resample by weeks
df = df.resample("W").sum()
# plot data
# plt.plot(df.index, df["Arrivals to Italy"])
# plt.show()
df = df.reset_index().rename(columns={'Date': 'ds', 'Arrivals to Italy': 'y'})

# Fit model
x_train = df[0:40]
x_test = df[40:]


# model = RandomForestRegressor(n_estimators=100,
#                                  max_features=1, oob_score=True)
# rgr=model.fit(X_train, Y_train)
# rgr.predict(X_test[0])


ph_model = fbprophet.Prophet(changepoint_prior_scale=0.15)
ph_model.fit(df[0:40])
ph_forecast = ph_model.make_future_dataframe(periods=14, freq='W')
ph_forecast = ph_model.predict(ph_forecast)

ph_model.plot(ph_forecast, xlabel = 'Date', ylabel = 'Market Cap (billions $)')
plt.title('Market Cap of GM')
plt.show()


pass