import requests
import json
import pandas as pd
import datetime_util as util

date_list = util.get_date_list("2022-01-01", "2022-02-20")
i = 1
for date in date_list:
    url = 'http://push2ex.eastmoney.com/getTopicZTPool'
    params = {
        'ut': '7eea3edcaed734bea9cbfc24409ed989',
        'dpt': 'wz.ztzt',
        'Pageindex': '0',
        'pagesize': '320',
        'sort': 'fbt:asc',
        'date': date.replace('-', ''),
        '_': '1621590489736',
    }
    r = requests.get(url, params=params)
    data_json = r.json()
    if data_json['data'] is not None:
        print(date, i)
        i = i + 1
        temp_df = pd.DataFrame(data_json['data']['pool'])
        df = temp_df.groupby("hybk").hybk.agg(['count'])
        sort_all = df.sort_values(by="count", ascending=False)
        print(sort_all)

# url = 'https://dc.qiumibao.com/shuju/public/index.php?_url=/index/league_v2&_platform=web&_env=pc'
# wbdata = requests.get(url).text
#
# data = json.loads(wbdata)
# news = data['data']['league']
#
# for n in news:
#     title = n['title']
#     img_url = n['image_url']
#     url = n['media_url']
#     print(url, title, img_url)
# 大于10往前推10个交易日 大于7个交易日在前五
#
