from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
from selenium.webdriver.common.by import By

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


x = loginUrl()
x.cleannuber()
x.WrongPassword()
x.cleannuber()
x.CorrectPpassword()


