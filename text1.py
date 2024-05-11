import requests
import urllib3
import time
import urllib.request
import urllib.parse
import random
from lxml import etree
import csv
import parsel

r1 = requests.get('https://www.sogou.com/',timeout=3)
print(r1)
print(r1.text)

r1.encoding='ISO-8859-1'
print(r1.encoding)

headers = {'User-Agent':'Mozilla/5.0 (windowsNT 10.0:WOW64) APPleWebKit/537.36(KHTML , like Gecko) Chrome/46.0.2490.80 Safari.537.36'}
url ='https://www.sogou.com/'
r=requests.get(url,headers=headers)
print(r.headers)
print(r1.history)
print(r1.url)

# r2 = requests.head('http://www.sogou.com/')
# print(r2)

print(r1.status_code)

 # payload= {'query', 'python'}
# r = requests.get('https://sogou.com/sie',params=payload)
# print(r.url)
     #https://www.sogou.com/sie?query=python&hdq=Af121264&ie=utf8&ekv=3&

payload = {'query':'python','cat':'1001'}
payload_encode = urllib.parse.urlencode(payload)
request_url ='https://sogou.com/sie'
request_url += '?' + payload_encode
response = urllib.request.urlopen(request_url)
# print(response.read().decode('urf-8'))
print(request_url)
print(response.geturl())
print(response.getcode())

#Xpath语法
import requests
from lxml import etree
htm="""
...<div>
...     <ul>
...         <li class="item-0"><a href="link1.html">first item</a></li>
...         <li class="item-1"><a href="link2.html">second item</a></li>
...         <li class="item-inactive"><a href="link3.html">third item</a></li>
...         <li class="item-1"><a href="link4.html">fourth item</a></li>
...         <li class="item-0"><a href="link5.html">fifth item</a></li>
...         <li class="else-0>else item</li>
            another item
...     </ul>
...</div>
..."""
selector = etree.HTML(htm)
all_li = selector.xpath('//div/ul/li')
print(all_li)
li_1 = selector.xpath('//div/ul/li[1]/a/text()')
print(li_1)
li_2 = selector.xpath('//div/ul/li[1]/a/text()')[0]
print(li_2)
#爬取百度
response = requests.get('https://www.baidu.com')
#print(response.encoding)#网站编码
response.encoding = 'utf-8'
selector = etree.HTML(response.text)
#//*[@id="s-top-left"]/a[1]
#
new_text = selector.xpath('//*[@id="u1"]/a[1]/text()')[0]
new_url = selector.xpath('//*[@id="u1"]/a[1]/@href')[0]
print(new_text)
print(new_url)
for a in range(10):
    ur1='https://movie.douban.com/top250?start={}&filter='.format(a*25)
    headers = {'User-Agent':'Mozilla/5.0 (windowsNT 10.0:WOW64) APPleWebKit/537.36(KHTML , like Gecko) Chrome/46.0.2490.80 Safari.537.36'}
    reap=requests.get(ur1,headers=headers).text
    #print(reap)

    htm1=etree.HTML(reap)
    lis=htm1.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for li in lis:
        title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a
        # //*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[1]/a
        # //*[@id="content"]/div/div[1]/ol/li[3]/div/div[2]/div[1]/a
        rating_num=li.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        #//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]
        #//*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[2]/div/span[2]
        #//*[@id="content"]/div/div[1]/ol/li[3]/div/div[2]/div[2]/div/span[2]
        pf=li.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0]
        href=li.xpath('./div/div[2]/div[1]/a/@href')[0]
        doct=li.xpath('./div/div[2]/div[2]/p[1]/text()[1]')[0]
        nianfen=li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')[0]
        #//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span
        inqa=li.xpath('./div/div[2]/div[2]/p[2]/span/text()')[0]



        #print(title,rating_num,href)
        time.sleep(0.2)
        print(title,rating_num,pf,href,doct,nianfen,inqa)


    with open(r'../书单', 'a', encoding='utf-8') as f:
        f.write('{},{},{},{},{},{},{}'.format(title,rating_num,pf,href,doct,nianfen,inqa))
        f.write('\n')