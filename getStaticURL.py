import re
import urllib.request
import os


# 获取网页源码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')


# 匹配正则表达式
def getUrl(html):
    reg = r' <a.+?href=\"(.+?)\".*>'
    urlre = re.compile(reg)
    urllist = urlre.findall(html)
    # f = open('D:/urllist', 'w', encoding='utf-8')
    # 匹配结果写入指定文件
    for urlre in urllist:
        print(urlre)
        # strf = str(urlre)
        # f.write(strf + '\n')


url = 'https://data.zhibo8.cc/pc_main_data/'
html = getHtml(url)
getUrl(html)
