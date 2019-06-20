import warnings
import itertools
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt

warnings.filterwarnings("ignore")


def grid_search_arima(series, search_range=None):
    """Find the best p, d and q values for time series.

    :param series: Time series
    :type series: DataFrame
    :param search_range: Maximum value range for p, d and q
    :type search_range: list
    :returns: tuple containing lowest aic and p,d and q combination
    """
    lowest = 100000
    lowest_combination = None
    if search_range is None:
        search_range = range(0, 5)
    p = d = q = search_range
    pdq = list(itertools.product(p, d, q))
    for combination in pdq:
        try:
            model = ARIMA(series, order=combination)
            arima_fit = model.fit()
        except:
            continue
        if arima_fit.aic <= lowest:
            lowest = arima_fit.aic
            lowest_combination = combination
    #         print(combination, arima_fit.aic)
    return (lowest_combination, lowest)

# root mean squared error
def measure_rmse(actual, predicted):
    return sqrt(mean_squared_error(actual, predicted))

