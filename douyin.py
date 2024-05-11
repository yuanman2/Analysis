# //*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div[1]
# //*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div[2]

import requests
import urllib3
import time
import urllib.request
import urllib.parse
import random
from lxml import etree
import csv
import parsel
from math import log
# import brotli


ur1='https://www.douyin.com/video/7169887023090650405'
headers={
    'Accept': 'application/json','Accept-Encoding': 'gzip',  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'cookie':'ttwid=1%7CDX4Vyl9WiNwZmzMy6jOIPN7xsZTdYErl1CbzwOLUaeI%7C1670472128%7C94b9e37c16bd65181ae27f33d1b25891120b714d7be0ba018762dca00335d782; home_can_add_dy_2_desktop=%220%22; s_v_web_id=verify_lbejz6g8_QxMnypyn_y8Zg_4Gzt_80QY_TMKsf2pwdyv8; passport_csrf_token=1d0fa4f37c4de7a47e0ab9602a36c807; passport_csrf_token_default=1d0fa4f37c4de7a47e0ab9602a36c807; ttcid=f4dafdf9fd8743a3be366c2974b92a4510; douyin.com; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20221208%22; __ac_nonce=06391fdef0042e5ac9894; __ac_signature=_02B4Z6wo00f01AxmqQQAAIDDY0ns.XeuHGgMRq2AAGCOOdbvXL9aL3BkMS7WBOZyru98RD29hIfss1O-frgnAxdR3a3.hxu4kJBQJrnOU2jOUUAjU1ty4hMODyB4scMm1dxEnTbZxPP2Lsgf53; msToken=Hctj2VeY2YEsqcMHc3r-Yiq3mSvpDsQEYsmIaBsI-Y_lLx8YtuBi908pANQPBov2GGw9mXWC1w3YDtEFLvtXJ5jNkraPc8dHVHCjwFukySM4t3ZErhPeoARPUN0O2meC; tt_scid=XnVM1v5G-DCnqqFGenVBQ8YaPH6piSmi4KRHzHO3OSLSNnUNbvcHvQjOOQKhltui7e55; passport_assist_user=CkDtLYjYjluf1xvAPgpaP0484MiypJ3XZwDVQA1FlN_WGeILXLDF9W8BPHhpWMM9UQJ4g9vdEbgfpCL_uJKjUmaSGkgKPCUx4quKqeTWlLXnHoKYrZhnWnILQqHeh-aGIBQxexXt8m5l6cEXMrgQM73RiECJ1-6CMzGF9_L_LHUSDhCbqqMNGImv1lQiAQNhKEO4; n_mh=cfLBiOnbg2BiSndspKeGyE9J7-iIqwHJwQSIc7In-6k; session_secure=1; sso_uid_tt=68945a9d9b3321ab6a37dc449ec26add; sso_uid_tt_ss=68945a9d9b3321ab6a37dc449ec26add; toutiao_sso_user=ac9b3896ee055f4839e172b58e519e57; toutiao_sso_user_ss=ac9b3896ee055f4839e172b58e519e57; sid_ucp_sso_v1=1.0.0-KDBiMjY2Yjc4MzhlZjE4MWRmNWFjZGQ5YjMzODU5YjgzODczMzE1OWIKHwj3vaD5gPS-ARDO_MecBhjvMSAMMPvmg-gFOAZA9AcaAmxxIiBhYzliMzg5NmVlMDU1ZjQ4MzllMTcyYjU4ZTUxOWU1Nw; ssid_ucp_sso_v1=1.0.0-KDBiMjY2Yjc4MzhlZjE4MWRmNWFjZGQ5YjMzODU5YjgzODczMzE1OWIKHwj3vaD5gPS-ARDO_MecBhjvMSAMMPvmg-gFOAZA9AcaAmxxIiBhYzliMzg5NmVlMDU1ZjQ4MzllMTcyYjU4ZTUxOWU1Nw; msToken=PLOD-vN6zc05OCOZPpdASXz_SGDBiLM9ALNancLItL7mb1oTDokvLNuQ1ZZuTj7iRBHdHhhn9_APy_xYiXl9bdRMNcJlBMdic4rFyygmZMK84j-P7NBlLCcGRORywZ-q; odin_tt=90ce04ad6fd3312388f6c905d2110de3ad95a468fd00245b784afcd47a0c6de819fa8fbf05a0eaf335b8e3fa6283d94b9f21ac91563a4156ccaf6d235609d323; passport_auth_status=6cdabfce171e5105df72398516929a39%2C; passport_auth_status_ss=6cdabfce171e5105df72398516929a39%2C; sid_guard=703c89090838a6c680dbd3be8eb7751c%7C1670512208%7C5183998%7CMon%2C+06-Feb-2023+15%3A10%3A06+GMT; uid_tt=2a3d203080912f63f4adaf4005f08287; uid_tt_ss=2a3d203080912f63f4adaf4005f08287; sid_tt=703c89090838a6c680dbd3be8eb7751c; sessionid=703c89090838a6c680dbd3be8eb7751c; sessionid_ss=703c89090838a6c680dbd3be8eb7751c; sid_ucp_v1=1.0.0-KGZjMjQ4MDk5OGM3YWJiMTEzZjAwOGRiM2MzZTgyZjUzZDI5Njc0NWIKGQj3vaD5gPS-ARDQ_MecBhjvMSAMOAZA9AcaAmhsIiA3MDNjODkwOTA4MzhhNmM2ODBkYmQzYmU4ZWI3NzUxYw; ssid_ucp_v1=1.0.0-KGZjMjQ4MDk5OGM3YWJiMTEzZjAwOGRiM2MzZTgyZjUzZDI5Njc0NWIKGQj3vaD5gPS-ARDQ_MecBhjvMSAMOAZA9AcaAmhsIiA3MDNjODkwOTA4MzhhNmM2ODBkYmQzYmU4ZWI3NzUxYw; strategyABtestKey=%221670512211.586%22'
}
# if response.headers[ "Content-Encoding"] == 'br':
#     resp_json = brotli.decompress(response.content)
# headers = { 'Accept': 'application/json',  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'DNT': '1', 'Host': 'xxx', 'Origin': 'https://xxx', 'Pragma': 'no-cache', 'Referer': 'https://xxx', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',  'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36' }
# bd-tt-error-code: 0
# content-encoding: br
# content-type: application/json; charset=utf-8
# cookie_ttwidinfo_webid: 7174623100452570682
# date: Thu, 08 Dec 2022 15:10:12 GMT
# eagleid: de51789516705122122214452e
# rip: [2605:340:cdb1:180:7f34:fe4:b6c7:47e6]:9290
# server: Tengine
# server-timing: inner; dur=272
# server-timing: cdn-cache;desc=MISS,edge;dur=66,origin;dur=296
# status: 200
# status_code: 0
# strict-transport-security: max-age=31536000; includeSubDomains
# timing-allow-origin: *
# to-cluster: high_read
# to-idc: lf
# tt_stable: 1
# vary: Accept-Encoding
# via: cache31.l2cm9-7[296,0], vcache1.cn4860[362,0]
# x-envoy-response-flags: -
# x-tt-logid: 202212082310120102080180371C225D24
# x-tt-trace-host: 01a90d5b9ee9ef0692dd55e92ea485d81ded546f5b949ce84dd8ec0a5bd0cbc1c2bfb2e1cb027ccad80ef2e993fa2d8ea865ae202de99a158a294ad7da90461398d52a935ac58e2129b67c817bd9c59e3a0d0c062a9c471d91099227c52ae345996376c4fdcd285ef06bd357b2031a50c0
# x-tt-trace-tag: id=3;cdn-cache=miss
# ttwid=1%7CDX4Vyl9WiNwZmzMy6jOIPN7xsZTdYErl1CbzwOLUaeI%7C1670472128%7C94b9e37c16bd65181ae27f33d1b25891120b714d7be0ba018762dca00335d782; home_can_add_dy_2_desktop=%220%22; s_v_web_id=verify_lbejz6g8_QxMnypyn_y8Zg_4Gzt_80QY_TMKsf2pwdyv8; passport_csrf_token=1d0fa4f37c4de7a47e0ab9602a36c807; passport_csrf_token_default=1d0fa4f37c4de7a47e0ab9602a36c807; ttcid=f4dafdf9fd8743a3be366c2974b92a4510; douyin.com; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20221208%22; __ac_nonce=06391fdef0042e5ac9894; __ac_signature=_02B4Z6wo00f01AxmqQQAAIDDY0ns.XeuHGgMRq2AAGCOOdbvXL9aL3BkMS7WBOZyru98RD29hIfss1O-frgnAxdR3a3.hxu4kJBQJrnOU2jOUUAjU1ty4hMODyB4scMm1dxEnTbZxPP2Lsgf53; msToken=Hctj2VeY2YEsqcMHc3r-Yiq3mSvpDsQEYsmIaBsI-Y_lLx8YtuBi908pANQPBov2GGw9mXWC1w3YDtEFLvtXJ5jNkraPc8dHVHCjwFukySM4t3ZErhPeoARPUN0O2meC; tt_scid=XnVM1v5G-DCnqqFGenVBQ8YaPH6piSmi4KRHzHO3OSLSNnUNbvcHvQjOOQKhltui7e55; passport_assist_user=CkDtLYjYjluf1xvAPgpaP0484MiypJ3XZwDVQA1FlN_WGeILXLDF9W8BPHhpWMM9UQJ4g9vdEbgfpCL_uJKjUmaSGkgKPCUx4quKqeTWlLXnHoKYrZhnWnILQqHeh-aGIBQxexXt8m5l6cEXMrgQM73RiECJ1-6CMzGF9_L_LHUSDhCbqqMNGImv1lQiAQNhKEO4; n_mh=cfLBiOnbg2BiSndspKeGyE9J7-iIqwHJwQSIc7In-6k; session_secure=1; sso_uid_tt=68945a9d9b3321ab6a37dc449ec26add; sso_uid_tt_ss=68945a9d9b3321ab6a37dc449ec26add; toutiao_sso_user=ac9b3896ee055f4839e172b58e519e57; toutiao_sso_user_ss=ac9b3896ee055f4839e172b58e519e57; sid_ucp_sso_v1=1.0.0-KDBiMjY2Yjc4MzhlZjE4MWRmNWFjZGQ5YjMzODU5YjgzODczMzE1OWIKHwj3vaD5gPS-ARDO_MecBhjvMSAMMPvmg-gFOAZA9AcaAmxxIiBhYzliMzg5NmVlMDU1ZjQ4MzllMTcyYjU4ZTUxOWU1Nw; ssid_ucp_sso_v1=1.0.0-KDBiMjY2Yjc4MzhlZjE4MWRmNWFjZGQ5YjMzODU5YjgzODczMzE1OWIKHwj3vaD5gPS-ARDO_MecBhjvMSAMMPvmg-gFOAZA9AcaAmxxIiBhYzliMzg5NmVlMDU1ZjQ4MzllMTcyYjU4ZTUxOWU1Nw; msToken=PLOD-vN6zc05OCOZPpdASXz_SGDBiLM9ALNancLItL7mb1oTDokvLNuQ1ZZuTj7iRBHdHhhn9_APy_xYiXl9bdRMNcJlBMdic4rFyygmZMK84j-P7NBlLCcGRORywZ-q; odin_tt=90ce04ad6fd3312388f6c905d2110de3ad95a468fd00245b784afcd47a0c6de819fa8fbf05a0eaf335b8e3fa6283d94b9f21ac91563a4156ccaf6d235609d323; passport_auth_status=6cdabfce171e5105df72398516929a39%2C; passport_auth_status_ss=6cdabfce171e5105df72398516929a39%2C; sid_guard=703c89090838a6c680dbd3be8eb7751c%7C1670512208%7C5183998%7CMon%2C+06-Feb-2023+15%3A10%3A06+GMT; uid_tt=2a3d203080912f63f4adaf4005f08287; uid_tt_ss=2a3d203080912f63f4adaf4005f08287; sid_tt=703c89090838a6c680dbd3be8eb7751c; sessionid=703c89090838a6c680dbd3be8eb7751c; sessionid_ss=703c89090838a6c680dbd3be8eb7751c; sid_ucp_v1=1.0.0-KGZjMjQ4MDk5OGM3YWJiMTEzZjAwOGRiM2MzZTgyZjUzZDI5Njc0NWIKGQj3vaD5gPS-ARDQ_MecBhjvMSAMOAZA9AcaAmhsIiA3MDNjODkwOTA4MzhhNmM2ODBkYmQzYmU4ZWI3NzUxYw; ssid_ucp_v1=1.0.0-KGZjMjQ4MDk5OGM3YWJiMTEzZjAwOGRiM2MzZTgyZjUzZDI5Njc0NWIKGQj3vaD5gPS-ARDQ_MecBhjvMSAMOAZA9AcaAmhsIiA3MDNjODkwOTA4MzhhNmM2ODBkYmQzYmU4ZWI3NzUxYw; strategyABtestKey=%221670512211.586%22
res=requests.get(ur1,headers=headers).text
    # print(reap)

reap = res[1:237000]
htm1=etree.HTML(reap)
# try:
#     log.info(
#         f"response len:{len(res.contenr)}")
#     if len(reap.content) < 230000:
#         log.info(
#             f"response:{sys._getframe().f_code.co_name}:{res.status_code} {res.json()}"
#         )
# except:
#     log.info('返回不是json')



# //*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div[1]
# //*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div[87]
# //*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div[21]
lis = htm1.xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div')
# try:
for li in lis:
    try:

        title = li.xpath('./div/div[2]/div/div[2]/div[1]/div/a/span/span/span/span/span/span/text()')[0]
        # /div/div[2]/div/p/span/span/span/span/span/span/span
        # /div/div[2]/div/p/span/span/span/span/span/span/span[1]
        # /div/div[2]/div/p/span/span/span/span/span/span/span[2]
        # comment = li.xpath('./div/div[2]/div/p/span/span/span/span/span/span/span')
        # try:
        # for li_li in comment:
        rating_num=li.xpath('./div/div[2]/div/p/span/span/span/span/span/span/span/text()')
        time.sleep(0.4)
        print(rating_num)

        if rating_num != ['防疫做的真好', '  果然是做到密不透风']:
            continue
    except:
        break
    print(title, rating_num)
            # print(title,rating_num)


    with open(r'douyin.csv', 'a', encoding='utf-8', newline='') as f:
        f.write('{},{}'.format(title,rating_num))
        f.write('\n')
# except:
#     pass


# except(IndexError):
#     continue

