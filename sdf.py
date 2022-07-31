from jqdatasdk import *
from statsmodels.tsa.stattools import adfuller
import pprint
# from numpy.random import *
import numpy as np


def hurst(ts):
    lags = range(2, 100)
    tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0] * 2.0


auth("13580430532", "Q1230321q")
gsyh = get_price("601398.XSHG", frequency='daily', fields=['close'])
# cadf = adfuller(gsyh['close'])
# pprint.pprint(cadf)
gbm = np.log(np.cumsum(np.random.randn(100000)) + 1000)
mr = np.log(np.random.randn(100000) + 1000)
tr = np.log(np.cumsum(np.random.randn(100000) + 1) + 1000)
# nm = np.cumsum(np.random.randn(10))
# print(nm)
print('Hurst(GBM): %s' % hurst(gbm))
print('Hurst(MR): %s' % hurst(mr))
print('Hurst(TR): %s' % hurst(tr))
print('Hurst(gsyh): %s' % hurst(gsyh.close.tolist()))
