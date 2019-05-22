import pandas as pd
import matplotlib.pyplot as plt

import fbprophet
from sklearn.ensemble.forest import RandomForestRegressor

excel_file = "datasets/20160921-analysisofestimatedarrivals.xlsx"

def load_data(file_name, skip_rows=14, cols=None):
    if cols is None:
        cols = [0, 1]
    df = pd.read_excel(file_name, skiprows=skip_rows, usecols=cols)
    headers = df.iloc[0]
    df = df[1:]
    df.columns = headers
    df["Date"] = pd.to_datetime(df["Date"])
    df =  df.set_index('Date')
    return df

df = load_data(excel_file)

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