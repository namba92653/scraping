from selenium import webdriver
from getpass import getpass
import time

driver = webdriver.Chrome('C:/Users/hirok/program/python/scrap/chromedriver.exe')

#ログイン(ID、password固定)
def login():
    user_id = "TwitterのユーザーID"  #ユーザーid入力
    password = "Twitterのパスワード"  #getpass()はターミナルで入力する際に、入力文字を表示させない関数です。

    #twitter投稿画面開く
    driver.get("https://twitter.com/login")

    # 3秒待つ
    time.sleep(3)

    #ID入力　
    username = driver.find_element_by_name("session[username_or_email]")
    username.send_keys(user_id)
    time.sleep(1)

    #パスワード入力
    passwordbox = driver.find_element_by_name("session[password]")
    passwordbox.send_keys(password)
    time.sleep(2)

    #ログイン
    element_login = driver.find_element_by_xpath("//div[contains(@data-testid,'LoginForm_Login_Button')]")
    element_login.click()
    time.sleep(3)


#ログイン(ID、password引数)
def every(user_id,password):

    #twitter投稿画面開く
    driver.get("https://twitter.com/login")

    # 3秒待つ
    time.sleep(3)

    #ID入力　
    username = driver.find_element_by_name("session[username_or_email]")
    username.send_keys(user_id)
    time.sleep(1)

    #パスワード入力
    passwordbox = driver.find_element_by_name("session[password]")
    passwordbox.send_keys(password)
    time.sleep(2)

    #ログイン
    element_login = driver.find_element_by_xpath("//div[contains(@data-testid,'LoginForm_Login_Button')]")
    element_login.click()
    time.sleep(3)


#ログイン(ID、password入力)
def everyone():
    user_id = input("ユーザーidを入力してください:")  #ユーザーid入力
    password = getpass("パスワードを入力してください:")  #getpass()はターミナルで入力する際に、入力文字を表示させない関数

    #twitter投稿画面開く
    driver.get("https://twitter.com/login")

    # 3秒待つ
    time.sleep(3)

    #ID入力　
    username = driver.find_element_by_name("session[username_or_email]")
    username.send_keys(user_id)
    time.sleep(1)

    #パスワード入力
    passwordbox = driver.find_element_by_name("session[password]")
    passwordbox.send_keys(password)
    time.sleep(2)

    #ログイン
    element_login = driver.find_element_by_xpath("//div[contains(@data-testid,'LoginForm_Login_Button')]")
    element_login.click()
    time.sleep(3)


#「i番目のツイートです」と投稿する
def four(i):
    four = driver.find_element_by_xpath("//div[contains(@data-testid,'tweetTextarea_0')]")
    four.click()
    four.send_keys(str(i)+"番目のツイートです")

    button = driver.find_element_by_xpath("//div[contains(@data-testid,'tweetButtonInline')]")
    button.click()


#引数に渡したものをツイートする
def hello(twing):

    hello = driver.find_element_by_xpath("//div[contains(@data-testid,'tweetTextarea_0')]")
    hello.click()
    hello.send_keys(twing)

    button = driver.find_element_by_xpath("//div[contains(@data-testid,'tweetButtonInline')]")
    button.click()


#chromeを閉じる
def quit():
    #5秒待つ
    time.sleep(5)

    #ブラウザ閉じる
    driver.quit()
