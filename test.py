import datetime
from datetime import date

import akshare as ak
import aktools as at
import pandas as pd
import numpy as np
stock_hot_rank_wc_df = ak.stock_zt_pool_em(date="20220712")
print(stock_hot_rank_wc_df.head())
# ak.bond_zh_hs_cov_min()
# stock_hot_rank_wc_df = ak.stock_hot_rank_wc(date="20220708")
# print(stock_hot_rank_wc_df.head(20))
# stock_zh_a_hist_pre_min_em = ak.stock_zh_a_hist_pre_min_em("002432")
# print(stock_zh_a_hist_pre_min_em)
# url = 'https://cdn.liaoxuefeng.com/static/img/loading.svg'
# print(url.split('/')[-1])
# print(date.strftime('2021-07', '%Y-%m'))
# print( datetime.datetime.strptime(str(datetime.datetime.now())[:7], "%Y-%m"))
# print('2021-07'.apply(lambda x: x.strftime('%Y-%m')).astype('datetime64'))

#
# df = pd.DataFrame([['Jay', 16, 'BBA'],
#                    ['Jack', 19, 'BTech'],
#                    ['Mark', 18, 'BSc']], columns=['Name', 'Age', 'Course'])
#
# d_records = df.to_dict('records')
# for x in d_records:
#     print(x['Name'])
# print(d_records[0])
# fund_em_new_found_df = ak.fund_em_new_found()
# print(fund_em_new_found_df.to_dict('records')[0])
# print(at.__version__)
# stock_zh_index_spot_df = ak.stock_zh_index_spot()
# print(np.nditer(stock_zh_index_spot_df.values, order='C'))
# print(stock_zh_index_spot_df.loc[0])
# stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sh000001")
# stock_em_zt_pool = ak.stock_em_zt_pool(date="20220224")
# dirdata = stock_em_zt_pool.to_dict('records')
# stock_zt_pool_em_df = ak.stock_zt_pool_em(date='20220622')
# print(stock_zt_pool_em_df)
# dirdata = stock_zt_pool_em_df.to_dict('records')
# print(stock_zt_pool_em_df)
# for x in dirdata:
#     print(x)
# print(stock_zh_index_daily_df)
# fund_hold_structure_em_df = ak.fund_hold_structure_em()
# print(fund_hold_structure_em_df)
#
# var = "#dt10;t2021_2;pi1;pn50;stasc;scbzdm"
#
# url = "http://fund.eastmoney.com/data/FundDataPortfolio_Interface.aspx"
# params = {
#     "dt": "10",
#     "t": "2021_2",
#     "pi": "1",
#     "pn": "50",
#     "st": "asc",
#     "sc": "bzdm",
# }

# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# print(df)
# print(df.values)
# df.values
