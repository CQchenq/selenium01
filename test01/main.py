from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
from selenium.webdriver.common.by import By
from functions import id,css,return_driver

wd = return_driver()
import time

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
url = 'http://admin-p2p-test.itheima.net/'
wd.get(url)
wd.maximize_window()
username = 'admin'
password = '123456'
valicode = '8888'
id('username').clear()
id('password').clear()
id('valicode').clear()
