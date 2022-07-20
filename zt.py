import requests
import pandas as pd
import datetime_util as date_util


# 主线延续性？
# 定义全局一个字典 {行业：时间}
# 一个月时间是否过期
# 大于10往前推10个交易日 大于7个交易日在前五 加入全局
# 重复行业时间延续5天
# 传入当前时间 赋值全局备选池
# trade={}

def getDailyLimit(day):
    url = 'http://push2ex.eastmoney.com/getTopicZTPool'
    params = {
        'ut': '7eea3edcaed734bea9cbfc24409ed989',
        'dpt': 'wz.ztzt',
        'Pageindex': '0',
        'pagesize': '320',
        'sort': 'fbt:asc',
        'date': str(day).replace("-", ""),
        '_': '1621590489736',
    }
    r = requests.get(url, params=params)
    data_json = r.json()
    if data_json['data'] is None:
        return
    return pd.DataFrame(data_json['data']['pool'])


def main():
    days = date_util.get_date_list('2022-01-04', '2022-01-10')
    for day in days:
        temp_df = getDailyLimit(day)
        print(day)
        if temp_df is not None:
            df_list = temp_df[temp_df['zttj'].apply(lambda x: dict(x)['days'] < 7) & temp_df['zttj'].apply(
                lambda x: dict(x)['ct'] > 4)]['c'].tolist()
            for item in range(0, len(df_list)):
                if df_list[item].startswith('6'):
                    df_list[item] = df_list[item] + '.XSHG'
                else:
                    df_list[item] = df_list[item] + '.XSHE'
            print("ces", df_list)


'''
File "/tmp/strategy/user_code.py", line 80, in before_trading_start
    check_stocks(context)
  File "/tmp/strategy/user_code.py", line 44, in check_stocks
    df_list = temp_df[temp_df['zttj'].apply(lambda x: dict(x)['days'] < 7) & temp_df['zttj'].apply(lambda x: dict(x)['ct'] > 4)]['c'].tolist()
TypeError: 'NoneType' object is not subscriptable
'''

# trade = {'通用设备': datetime.date(2022, 6, 28), '汽车零部': datetime.date(2022, 7, 1)}
# days = get_trade_days(end_date=datetime.date.today(), count=5)
# for day in days:
#     # 判断是否过期
#     trade = {k: v for k, v in trade.items() if v != datetime.date.today()}
#     #     print('判断是否过期',trade)
#     temp_df = getDailyLimit(day)
#     print(temp_df.head())
#     if temp_df is None:
#         continue
#     df = temp_df.groupby("hybk").hybk.agg(['count'])
#     sort_all = df.sort_values(by="count", ascending=False)
#     # 过滤大于10行业
#     sort = list(sort_all[sort_all['count'] >= 10].index)
#     trade_new = {}
#     for k, v in trade.items():
#         if k in sort:
#             trade[k] = v + datetime.timedelta(days=2)
#     #     print(list(trade.keys()))
#     for s in sort:
#         if s not in trade.keys():
#             # 往前推10个交易日
#             before_days = get_trade_days(end_date=datetime.date.today(), count=10)
#             i = 0
#             for before in before_days:
#                 temp = getDailyLimit(before)
#                 if temp is None:
#                     continue
#                 hybk = temp.groupby("hybk").hybk.agg(['count'])
#                 sort_hybk = hybk.sort_values(by="count", ascending=False)
#                 industry = sort_hybk['count'].index[:5]
#                 #                 print(s)
#                 #                 print(industry)
#                 if s in industry:
#                     i = i + 1
#             if i >= 5:
#                 trade_new[s] = day
#     trade.update(trade_new)
#
#     df_list = []
#     for index in trade.keys():
#         print(index)
#         df_list.append(list(temp_df[temp_df["hybk"].str.contains(index)]['c']))
#     one_list = [item for i in df_list for item in i]
#     result = []
#     for a in one_list:
#         if a.startswith('6'):
#             result.append(a + '.XSHG')
#         else:
#             result.append(a + '.XSHE')
if __name__ == '__main__':
    main()
