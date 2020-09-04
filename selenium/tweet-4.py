"""
「0～3番目のツイートです」と4ツイートする。
"""

from selenium import webdriver
import tweeting
import time

tweeting.login()

#複数ツイート処理
for i in range(4):
    tweeting.four(i)
    time.sleep(5)

tweeting.quit()
