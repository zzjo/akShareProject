import numpy as np
import pandas as pd

dates = pd.date_range('2/6/2022', periods=5, freq='D')
df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
print(df[-2])
# times = [935, 940, 945, 950, 955, 1000, 1005, 1010, 1015,
#          1020, 1025, 1030, 1035, 1040, 1045, 1050, 1055,
#          1100, 1105, 1110, 1115, 1120, 1125, 1130, 1305,
#          1310, 1315, 1320, 1325, 1330, 1335, 1340, 1345,
#          1350, 1355, 1400, 1405, 1410, 1415, 1420, 1425,
#          1430, 1435, 1440, 1445, 1450, 1455, 1500]
#
# print(times.index(935))
