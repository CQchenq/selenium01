from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'F:\chromedriver_win32\chromedriver.exe'))
def id(element):
    return wd.find_element(By.ID,element)

# 通过 CSS 获取元素
def css(element):
    return wd.find_element(element)

def return_driver():
    return wd
