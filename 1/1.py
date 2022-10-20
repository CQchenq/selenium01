from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome(service=Service(r'F:\chromedriver_win32\chromedriver.exe'))
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
url = 'http://admin-p2p-test.itheima.net/'
wd.get(url)
wd.maximize_window()
username = 'admin'
password = '123456'
valicode = '8888'
class loginUrl:
    def __init__(self):
       pass
    #清除账号密码
    def cleannuber(self):
        self.username = wd.find_element(By.ID, 'username').clear()
        self.password = wd.find_element(By.ID, 'password').clear()
        self.valicode = wd.find_element(By.ID, 'valicode').clear()
        print("清除输入框内容")
    # 输入错误的账号密码
    def WrongPassword(self):
        wd.find_element(By.ID, 'username').send_keys('chenq')
        wd.find_element(By.ID, 'password').send_keys('12345')
        wd.find_element(By.ID, 'valicode').send_keys('8888')
        wd.find_element(By.CLASS_NAME, 'login-button').click()
        print("用户名密码错误")
    # 输入正确的账号密码
    def CorrectPpassword(self):
        wd.find_element(By.ID, 'username').send_keys(username)
        wd.find_element(By.ID, 'password').send_keys(password)
        wd.find_element(By.ID, 'valicode').send_keys(valicode)
        wd.find_element(By.CLASS_NAME, 'login-button').click()
        print("登录成功，进入首页")
        time.sleep(3)
    #在所有贷款中进行操作
    def AllBorrowings(self):
        wd.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[1]/a').click()
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[1]/ul/li[1]/a').click()
        time.sleep(1)
        #frame窗口切换
        wd.switch_to.frame('iframe_box')
        wd.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[1]/div/input').send_keys('19800001111')
        wd.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/div/input').send_keys('张三买汽车')
        wd.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[3]/div/input').send_keys('202210200020')
        js1 = "$('input:eq(3)').removeAttr('readonly')"  #删除日期窗口的readonly
        js2 = "$('input:eq(4)').removeAttr('readonly')"  #删除日期窗口的readonly
        wd.execute_script(js1)
        wd.execute_script(js2)
        wd.find_element(By.XPATH, '//*[@id="startTime"]').send_keys('2021-10-19')
        wd.find_element(By.XPATH, '//*[@id="endTime"]').send_keys('2022-10-20')
        time.sleep(1)
        wd.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[6]/div/select').click()
        wd.find_elemaent(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[6]/div/select/option[2]').click()
        time.sleep(1)
        wd.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[7]/div/select').click()
        wd.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[7]/div/select/option[2]').click()
        time.sleep(1)
        wd.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[8]/div/select').click()
        wd.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/ul/li[8]/div/select/option[10]').click()
        wd.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[9]/input').click()
x = loginUrl()
x.cleannuber()
x.WrongPassword()
x.cleannuber()
x.CorrectPpassword()
x.AllBorrowings()


