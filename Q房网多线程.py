from multiprocessing.dummy import Pool as pl
from lxml import etree
import requests
import csv

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64'
                        'AppleWebKit/537.36 (KHTML,like Gecko'
                        'Chrome/46.0.2490.80 Safari/537.36'}
pre_url = 'http://shenzhen.qfang.com/sale/f'

def download(url):
    html = requests.get(url,headers = headers)
    return etree.HTML(html.text)

def data_writer(itrm):
    with open('qfang_ershoufang.csv','a',encoding = 'utf-8', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)

def image_saver(url,xiaoqu):
    img = requests.get(url,headers = headers)
    with open('./Qfang_image/{}.jpg'.format(apartment),'wb') as f:
        f.write(img.content)

def spider(url):
    selector = download(url)
    house_list = selector.xpath("//*@id='cycleListings']/ul/li")
    for house in house_list:
        apartment = house.xpath("div[1]/p[1]/a/text()")[0]
        house_layout = house.xpath("div[1]/p[2]/span[2]/text()")[0]
        area = house.xpath("div[1]/p[2]/span[4]/text()")[0]
        region = house.xpath("div[1]/p[3]/span[2]/a[1]/text()")[0]
        total_price = house.xpath("div[2]/span[1]/span[1]/text()")[0]
        #构造详情页URL
        house_url = ('http://shenzhen.qfang.com'
                     + house.xpath("div[1]/p[1]/a/@href")[0])
        sel = download(house_url)
        house_year = sel.xpath("//div[@class='housing-info']/ul/li[2]"
                               "/div/ul/li[3]/div/text()")[0]
        mortgage_info = sel.xpath("//div[@class='housing-info']/ul/li[2]"
                                  "div/ul/li[5]/div/text()")[0]
        item = [apartment,house_layout,area,region,total_price,house_year,mortgage_info]
        data_writer(item)
        print('正在抓取',xiaoqu)
        image_url = house.xpath('a/img/@data-original')[0]
        image_saver(image_url,xiaoqu)


if __name__ == '__main__':
    pool = pl(4)