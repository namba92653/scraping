"""
入力した内容をツイートする。tweet-1と違ってID、パスワードが自由
"""

from selenium import webdriver
import tweeting
import time

#ツイート内容入力
twing = input("ツイート内容を入力してください:")

tweeting.everyone()
tweeting.hello(twing)
tweeting.quit()
