"""
ツイート内容、ID、パスワードをGUIで入力する。
"""

from selenium import webdriver
import tweeting
import time
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#実行ボタンの動作
def app():
    tweeting.every(folder_box.get(),folder_box2.get())
    tweeting.hello(folder_box3.get())
    main_win.destroy()
    tweeting.quit()


# メインウィンドウ
main_win = tkinter.Tk()
main_win.title("ツイートする")
main_win.geometry("500x120")

# メインフレーム
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)


# ウィジェット作成
folder_label = ttk.Label(main_frm, text="ID")
folder_box = ttk.Entry(main_frm)

folder_label2 = ttk.Label(main_frm, text="パスワード")
folder_box2 = ttk.Entry(main_frm)

folder_label3 = ttk.Label(main_frm, text="ツイート内容")
folder_box3 = ttk.Entry(main_frm)

app_btn = ttk.Button(main_frm, text="実行", command=app)


# ウィジェットの配置
folder_label.grid(column=0, row=0, padx=5)
folder_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
folder_label2.grid(column=0, row=1, padx=5)
folder_box2.grid(column=1, row=1, sticky=tkinter.EW, padx=5)
folder_label3.grid(column=0, row=2, padx=5)
folder_box3.grid(column=1,row=2, sticky=tkinter.EW, padx=5)
app_btn.grid(column=1, row=3)


# 配置設定
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

main_win.mainloop()
