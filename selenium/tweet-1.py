"""
入力した内容をツイートする。
"""

from selenium import webdriver
import tweeting
import time

#ツイート内容入力
twing = input("ツイート内容を入力してください:")

tweeting.login()
tweeting.hello(twing)
tweeting.quit()
