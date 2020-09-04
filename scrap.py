"""
サイトのタイトルを取得してきてslackに通知する。
"""

import feedparser
import slackweb

#スクレイピングするサイトのフィードを入力
sitefeed=input()

#解析
d = feedparser.parse(sitefeed)

#slackへ通知
for entry in d.entries:
    slack = slackweb.Slack(url="webhookで取得してきたslackのURLを書く")
    slack.notify(text =entry.title)
  
