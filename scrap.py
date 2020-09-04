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
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    slack.notify(text =entry.title)
