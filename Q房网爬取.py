from lxml import etree
import requests
import csv
import time

def spider():
    #定义爬虫头部
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0;WOW64) '
                            'AppleWebKit/537.36 (KHTML,lie Gecko)'
                            'Chrome/46.0.2490.80 Safari/537.36'}
    #这里使用for循环构造钱10页URL地址并GET请求下载
    #未来防止爬行速度过快，在每一次GET后，等待2秒
    pre_url = 'http://shenzhen.qfang.com/sale/f'
    for x in range(1,11):
        html = requests.get(pre_url + str(x),headers = headers)
        time.sleep(2)
        #用获取到的页面初始化etree，得到一个selector
        #然后在这个selector上使用XPath提取数据
        selector = etree.HTML(html.text)

        #先获取房源列表
        house_list = selector.xpath("//*[@id='cycleListings']/ul/li")
        for house in house_list:
            apartment = house.xpath("div[1]/p[1]/a/text()")[0]
            house_layout = house.xpath("div[1]/p[2]/span[2]/text()")[0]
            area = house.xpath("div[1]/p[2]/span[4]/text()")[0]
            region = house.xpath("div[1]/p[3]/span[4]/text()")[0]
            total_price = house.xpath("div[2]/span[1]/text()")[0]

    item = [apartment,house_list,area,region,total_price]
    data_writer(item) #保存数据
    print('正在抓取',xiaoqu)

        #保存爬取到的信息
def data_writer(item):
    with open('qfang_ershoufang.csv','a',encoding = 'utf-8',newline = '') as csvfile:
        writer = csv.weiter(csvfile)
        writer.writerow(item)

if __name__ =='__main__':
    spider()