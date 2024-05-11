import requests
from lxml import etree
import csv
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64'
                        'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/46.0.2490.80 Safari/537.36'}
pre_url = 'http://shenzhen.qfang.com/sale/f'
def dowmload(url):
    html = requests.get(url,headers = headers)
    timie.sleep(2)
    return etree.HTML(html.text)

def data_writer(item):
    with open('qfang_ershoufang.csv','a',encoding = 'utf-8',newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)


    def spider(list_url):
        selector - download(list_url)
        house_list = delector.xpath("//*@id='cycleListings']/ul/li")
        for house in house_list:
            apartment = house.xpath("div[1]/p[1]/a/text()")[0]
            house_layout = house.xpath("div[1]/p[2]/span[2]/text()")[0]
            area = house.xpath("div[1]/p[2]/span[4]/text()")[0]
            region = house.xpath("div[1]/p[3]/span[2]/a[1]/text()")[0]
            total_price = house.xpath("div[2]/span[1]/text()")[0]
            #构造详情页URL
            house_url = ('http://shenzhen.qfang.con'
                         + house.xpath("div[1]/p[1]/a/@href")[0])
            sel = download(house_url)
            time.sleep(1)
            house_years = sel.xpath("//div[@class='housing-info']/ul"
                                    "/li[2]/div/ul/li[3]/div/text()")[0]
            mortgage_info = sel.xpath("//div[@class='housing-info']/ul"
                                     "/li[2]/div/ul/li[5]/div/text()")[0]
            item = [apartment,house_list,area,region,total_price,house_years,mortgage_info]
            print('正在抓取',apartment)
            data_writer(item)

        if __name__ == '__main__':
            for x in range(1,11):
                spider(pre_url + str(x))