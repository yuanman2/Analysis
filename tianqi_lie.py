import csv
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
import string
riqi_1 = []  #日期
temp_hight = [] #最高气温
temp_low = []   #最低气温
riqi = []   #日期
qiwen_higth = []    #最高气温
qiwen_low = []      #最低气温
tianqi_new = []     #天气—1
tianqi_old = []     #天气-2
fenli_new = []      #风向
fenli_old = []      #风力
def spider_look(url_list):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;WOW64) '
                             'AppleWebKit/537.36 (KHTML,lie Gecko)'
                             'Chrome/46.0.2490.80 Safari/537.36'
               }
    cookies = 'ASP.NET_SessionId=sk0wloune1kpne45do2rweat; __51cke__=; __tins__4560568=%7B%22sid%22%3A%201702133587496%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201702135387496%7D; __tins__21287555=%7B%22sid%22%3A%201702135068287%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201702136868287%7D; __51laig__=7'

    for url in url_list: #= 'http://www.tianqihoubao.com/lishi/xian/month/201101.html'
        print(url)
        # response_12 = requests.get(url = url,headers = headers,timeout = 8,cookies = cookies)
        response_12 = requests.get(url=url, headers=headers, timeout=30)
        soup = BeautifulSoup(response_12.text, 'html.parser')
        # print(soup.prettify())
        # print(soup.tbody)

        # date_1 = soup.find_all('tr')[1].get_text()
        # data_2 = date_1.split( )
        # ['日期', '天气状况', '最低气温/最高气温', '风力风向(夜间/白天)']
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


        # 列式储存

        for i in range(0,32):
            try:
                date_1 = soup.find_all('tr')[i].get_text()
        # date_1 = soup.find_all('tr')[1].get_text()
                data_2 = date_1.split()
                print(data_2)
                if i == 0:
                    continue
                else:
                    for n in range(0,10):
                        if n == 0:
                            riqi_1 = data_2[n]
                            riqi.append(riqi_1)
                            # print(riqi)

                        elif n == 1:
                            tianqi_1 = data_2[n]
                            tianqi_new.append(tianqi_1)
                            # print(tianqi_new)
                        elif n == 2:
                            tianqi_2 = data_2[n][1:]
                            tianqi_old.append(tianqi_2)
                            # print(tianqi_old)

                        elif n == 3:
                            low_1 = data_2[n]
                            qiwen_low.append(low_1)
                            # print(qiwen_low)
                        elif n == 5:
                            low_2 = data_2[n]
                            qiwen_higth.append(low_2)
                            # print(qiwen_higth)
                        elif n == 8:    #风向
                            lfenli_1 = data_2[n][1:]
                            fenli_new.append(lfenli_1)
                            # print(fenli_new)
                        elif n == 9:
                            lfenli_2 = data_2[n]
                            fenli_old.append(lfenli_2)
                            # print(fenli_old)
                        else:
                            continue


                    # print(n)



        # ['2011年01月01日', '阴', '/小雪', '-4℃', '/', '3℃', '旋转风', '微风', '/东风', '微风']
            except:
                break
        # print('正在抓取第%d天的数据' % i)
        # print(riqi)
        table_date = data_Frame()
        data_writer(table_date)
    # read_np_look()

# print(riqi)         #日期
# print(qiwen_higth)  #最高气温
# print(qiwen_low)     #最低气温
# print(tianqi_new)   #天气—1
# print(tianqi_old)     #天气-2
# print(fenli_new)     #风向
# print(fenli_old)    #风力



# 使用DataFrame转化为二维数组
def data_Frame():       #该方法只能spider()使用
    data = {'riqi':riqi,'qiwen_hight':qiwen_higth,'qiwen_low':qiwen_low,'tianqi_new':tianqi_new}
    df = pd.DataFrame(data)
    print(df)
    return df

    # print(df)

#将二维数组写入文件中
def data_writer(table_date):
    table_date.to_csv("xian_tianqi_lie.csv",index=False,encoding = 'utf-8')
    print('数据写入成功')
#pandas读取数据方法
def read_pd():
    df = pd.read_csv(r'xian_tianqi_lie.csv',na_values='N/A',encoding = 'utf-8')
    print('数据读取成功')
#numpy读取数据方法
def read_np_look():
    # df = np.genfromtxt('xian_tianqi_lie.csv',delimiter = ',',encoding = 'utf-8',dtype= str)
#     loadtxt可以跳过第一行
    df = np.loadtxt('xian_tianqi_lie.csv',delimiter = ',',encoding = 'utf-8',skiprows = 1,dtype= str)
    for i in range(len(df)):
        # print(df[i][1])
        for j in range(len(df[1])):
            if j == 0:
                riqi_1.append(df[i][j])
            elif j == 1:
                a = df[i][j].replace('℃', '')
                temp_hight.append(int(a))
            elif j == 2:
                b = df[i][j].replace('℃', '')
                temp_low.append(int(b))
            else:
                continue
    # look_look(riqi_1, temp_hight, temp_low)


def look_look(riqi_1,temp_hight,temp_low):
    x = np.arange(1,len(riqi_1)+1)
    y_1 = np.array(temp_hight)
    y_2 = np.array(temp_low)
    plt.title('天气变化')
    plt.xlabel('日期')
    plt.ylabel('气温变化')
    plt.plot(x,y_1)
    plt.plot(x,y_2)
    plt.show()


if __name__ == '__main__':
    url_list = [
        'http://www.tianqihoubao.com/lishi/xian/month/202201.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202202.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202203.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202204.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202205.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202206.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202207.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202208.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202209.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202210.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202211.html',
        'http://www.tianqihoubao.com/lishi/xian/month/202212.html'
    ]       #url列表，列表元素必须为字符串
    spider_look(url_list)
    read_np_look()
    look_look(riqi_1, temp_hight, temp_low)


