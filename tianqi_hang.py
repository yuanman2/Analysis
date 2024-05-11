import csv

import requests
from bs4 import BeautifulSoup
import string



def spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)) '
                             'AppleWebKit/537.36 (KHTML, like Gecko))'
                             'Chrome/119.0.0.0 Mobile Safari/537.36 Edg/119.0.0.0'
               }
    # Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 Edg/119.0.0.0

    Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'

    cookies = 'ASP.NET_SessionId=sk0wloune1kpne45do2rweat; __51cke__=; __tins__4560568=%7B%22sid%22%3A%201702133587496%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201702135387496%7D; __tins__21287555=%7B%22sid%22%3A%201702186509461%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201702188309461%7D; __51laig__=9'

    url = 'http://www.tianqihoubao.com/lishi/xian/month/201101.html'
    response_12 = requests.get(url = url,headers = headers,timeout = 8)
    soup = BeautifulSoup(response_12.text, 'html.parser')
    print(soup.prettify())
    # print(soup.tbody)

    # date_1 = soup.find_all('tr')[1].get_text()
    # data_2 = date_1.split( )
    # ['日期', '天气状况', '最低气温/最高气温', '风力风向(夜间/白天)']
    # ['2011年01月01日', '阴', '/小雪', '-4℃', '/', '3℃', '旋转风', '微风', '/东风', '微风']
    # 列式储存
    data_list = []      #数据
    list_head = []      #列头
    for i in range(0,32):
        try:
            date_1 = soup.find_all('tr')[i].get_text()
    # date_1 = soup.find_all('tr')[1].get_text()
            data_2 = date_1.split()
            print(data_2)
            if i == 0:
                list_head = data_2
                continue
            else:
                for n in range(0,10):
                    if n == 0:
                        riqi_1 = data_2[n]
                        data_list.append(riqi_1)
                        # print(riqi)

                    elif n == 1:
                        tianqi_1 = data_2[n]
                        data_list.append(tianqi_1)
                        # print(tianqi_new)
                    elif n == 2:
                        tianqi_2 = data_2[n][1:]
                        data_list.append(tianqi_2)
                        # print(tianqi_old)

                    elif n == 3:
                        low_1 = data_2[n]
                        data_list.append(low_1)
                        # print(qiwen_low)
                    elif n == 5:
                        low_2 = data_2[n]
                        data_list.append(low_2)
                        # print(qiwen_higth)
                    elif n == 8:    #风向
                        lfenli_1 = data_2[n][1:]
                        data_list.append(lfenli_1)
                        # print(fenli_new)
                    elif n == 9:
                        lfenli_2 = data_2[n]
                        data_list.append(lfenli_2)
                        # print(fenli_old)
                    else:
                        continue
                print('正在抓取第%d天的数据',n)
                print(data_list)
                data_writer(data_list)
                data_list.clear()       #清除之前数据

        except:
            break

        print('正在抓取第%d天的数据' % i)
        print(data_list)
        # data_list_1 = data_list.reverse #反转列
        # data_writer(data_list_1)
        data_writer(data_list)
        data_list.clear()  # 清除之前数据
# 转换为字符
# print(soup.find_all('tr')[1].string)
# None

# for i in range(0,32):
#     date_1 = soup.find_all('tr')[i].get_text()
#     print(date_1.split( ))
# #                                            2011年01月02日
#
#
#                                         小雪
#                                         /阴
#                                         -6℃
#                                         /
#                                         0℃
#
#                                         旋转风 微风
#                                         /无持续风向 微风

# print(date_1.split())
# data_3 = data_2.pop(4) 删除第5个元素
# def remove_punctuation(list):  #该方法传列表参数
#     new_list = []
#     for item in list:
#         if item.isalnum(): #判断是否为字母或数字
#             new_list.append(item)
#     return new_list #去除字符和数字  ——————不可用，含温度
#
#
# data_4 = remove_punctuation(data_2)
# data_5 = data_2[2],data_2[7] = data_2[1][:-1],data_2[1][:-1]
#写入csv文件
def data_writer(item):
    with open('xian_tianqi.csv','a',encoding = 'utf-8',newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)


if __name__ == '__main__':
    spider()