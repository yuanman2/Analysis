import requests
import urllib3
import time
import urllib.request
import urllib.parse
import random
from lxml import etree
import csv
import parsel

for a in range(10):
    ur1='https://m.lianjia.com/bj/jingjiren/?page_size=15&_t=1&offset='.format(a*25)
    headers = {'User-Agent':'Mozilla/5.0 (windowsNT 10.0:WOW64) APPleWebKit/537.36(KHTML , like Gecko) Chrome/46.0.2490.80 Safari.537.36'}
    reap=requests.get(ur1,headers=headers).text
    # print(reap)

    # for a in range(1, 200):
    #     a = a + 2
    #     agent_list = sel.xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[a]')

    htm1=etree.HTML(reap)
    # for a in range(1, 200):
        # for i in range(100):
    # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]
    lis = htm1.xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div')
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[31]
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[33]
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[35]
        # a = a + 2

    for li in lis:
        try:
            title = li.xpath('./div[1]/div/div/div[2]/div[1]/span/text()')[0]
            rating_num=li.xpath('./div[1]/div/div/div[2]/p/text()')[0]
            time.sleep(0.4)
            print(title,rating_num)


            with open(r'lianjiabiao.csv', 'a', encoding='utf-8') as f:
                f.write('{},{}'.format(title,rating_num))
                f.write('\n')
        except:
            pass