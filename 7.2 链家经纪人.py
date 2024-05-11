import requests
import urllib3
import time
import urllib.request
import urllib.parse
import random
# from lxml import etree
import csv
from lxml import etree
import parsel

item=[]
def csv_writer(item):
    with open(r'lianji_jingbiao.csv', 'a', encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)
        # csv.write('{},{}'.format(agent_name,agent_region))
        # csv.write('\n')




def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    response = requests.get(url, headers=headers).text
    sel = etree.HTML(response)
    # print(sel)
    for i in range(1,200):
        i=i+2
        agent_list = sel.xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[i]')
    # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[279]
        for agent in agent_list:
            agent_name = agent.xpath('./div[1]/div/div/div[2]/div[1]/span/text()')[0]
        #     //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/span
        #     //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/span[1]
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[279]/div/div/div/div[2]/div[1]/span[1]
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/span
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div/div[2]/div[1]/span
            agent_region = agent.xpath('./div[1]/div/div/div[2]/p/text()')[0]
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[141]/div/div/div/div[2]/p
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/p
        # //*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div/div[2]/p
        # item = [agent_name, agent_region]
            print('正在爬取：', agent_name,agent_region)
            csv_writer(item)



if __name__ == '__main__':
    for i in range(1, 3):
        # https://m.lianjia.com/bj/jingjiren/?page_size=15&_t=1&offset=
        # https://m.lianjia.com/bj/jingjiren/?page_size=15&_t=1&offset=
        # https://m.lianjia.com/bj/jingjiren/ao12pg3?page_size=15&_t=1&offset=
        # https://m.lianjia.com/bj/jingjiren/ao12pg4?page_size=15&_t=1&offset=
        url='https://m.lianjia.com/bj/jingjiren/?page_size=15&_t=1&offset='.format(i*25)
        # url = 'https://m.lianjia.com/bj/jingjiren/ao12pg' + str(i) + 'page_size=15&_t=1&offset='
        spider(url)
