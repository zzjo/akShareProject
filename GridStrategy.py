from MyTT import *
from akshare import *
from datetime import *

endDateStr = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
startDateStr = datetime.strftime(datetime.now() - timedelta(minutes=20), "%Y-%m-%d %H:%M:%S")
print(startDateStr)

bond_zh_hs_cov_min(symbol='000001', period='1', start_date='')
