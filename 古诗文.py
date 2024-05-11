from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time
import os

web = Chrome() # 将浏览器变成一个可执行变量
web.get("https://so.gushiwen.cn/user/collect.aspx")
img = web.find_element(by=By.XPATH, value="/html/body/form[1]/div[4]/div[4]/img").screenshot_as_png
chaojiying = Chaojiying_Client('13227024901', '123456', '935077')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']  # 返回的是一个字典，我们需要的是字典里pic_str的值
print(verify_code)

web.find_element(by=By.XPATH, value="/html/body/form[1]/div[4]/div[2]/input[2]").send_keys("1214694965@qq.com")  # 填写账号
web.find_element(by=By.XPATH, value="/html/body/form[1]/div[4]/div[3]/input").send_keys("123456")  # 填写密码
# web.find_element_by_xpath("/html/body/form[1]/div[4]/div[4]/input").send_keys(verify_code)#填写验证码  这里显示被弃用是因为版本不一样
web.find_element(by=By.XPATH, value="/html/body/form[1]/div[4]/div[4]/input").send_keys(verify_code)  # 填写验证码
time.sleep(2)
web.find_element(by=By.XPATH, value="/html/body/form[1]/div[4]/div[6]/input").click()  # 点击登录

web.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/a[2]").click()
web.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/a[1]").click()

buttons = web.find_elements(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div/span[1]/a")

for button in buttons:
    button.click()
    time.sleep(1)
    web.switch_to.window(web.window_handles[-1]) # 完成页面的切换
    content_title = web.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/h1").text  # 标题
    content_author = web.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/p").text  # 作者 朝代
    content_content = web.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div[1]/div[2]").text  # 内容

    with open("古诗文.txt","a",encoding="utf_8") as f:
        f.write("{},{},{},{},{}".format(content_title,content_author,"\n",content_content,"\n"))
        print(content_title,"保存成功！")
    web.close()
    web.switch_to.window(web.window_handles[0])