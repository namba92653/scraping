import time
from selenium import webdriver

# Chromeブラウザを起動する
driver = webdriver.Chrome('C:/Users/hirok/program/python/scrap/chromedriver.exe')

# Googleのサイトを開く
driver.get("https://www.google.co.jp/")

# 検索欄に「python」と入力する
search_box = driver.find_element_by_name('q')
search_box.send_keys('python')

# 検索する
search_box.submit()
