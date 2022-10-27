from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'F:\chromedriver_win32\chromedriver.exe'))
#通过 id 获取元素
def id(element):
    return wd.find_element(By.ID,element)

# 通过 CSS 获取元素
def css(element):
    return wd.find_element(By.CSS_SELECTOR,element)

# 通过 xpath 获取元素
def css(element):
    return wd.find_element(By.XPATH,element)

# 通过 partial_link_text 获取元素
def css(element):
    return wd.find_element(By.PARTIAL_LINK_TEXT,element)

# 通过 link_text 获取元素
def css(element):
    return wd.find_element(By.LINK_TEXT,element)

# 通过 tag_name 获取元素
def css(element):
    return wd.find_element(By.TAG_NAME,element)

# 通过 class_name 获取元素
def css(element):
    return wd.find_element(By.CLASS_NAME,element)

# 通过 by_name 获取元素
def css(element):
    return wd.find_element(By.NAME,element)

def return_driver():
    return wd
