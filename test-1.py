import requests
import urllib
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
import asyncio
# スクレイピング対象
#URL = 'https://www.tvkingdom.jp/chart/23.action'
URL='https://bangumi.org/epg/td?ggm_group_id=42'

# WordPress接続情報
WP_URL = 'https://xxxx.com'
WP_USERNAME = 'userName'
WP_PASSWORD = 'xxxx xxxx xxxx xxxx xxxx xxxx'

ARTICLE_ID = "9999"


# WordPress更新関数
def post_article(id, content):

    # REST APIを使うための認証情報
    user_ = WP_USERNAME
    pass_ = WP_PASSWORD
    # 更新情報
    payload = {"content": content}      #内容
               
    # 記事の更新を行う
    res = requests.post(urllib.parse.urljoin(WP_URL,  "wp-json/wp/v2/posts/" + id),     #"wp-json/wp/v2/posts/<id>"にPostすると更新になる
                        json=payload,                                                   #投稿する記事の内容を設定する
                        auth=(user_, pass_))                                            #ユーザとアプリケーションパスワードを設定する
    print('WP投稿結果:{}'.format(res))
    return res


nest_asyncio.apply()

# セッション開始
session = HTMLSession()
r = session.get(URL)
# ブラウザエンジンでHTMLを生成させる
r.text


content = '香川真司と久保建英の最新ニュースです。'


elems = r.html.find(".program_text")

for i,elem in enumerate(elems):
    href = elem.find('a')
    # ５件だけ処理する
    if i==5:
        break
    link_ = href[0].attrs['href']
    # 抽出したURLを整形して絶対パスを作る
    link = 'https://bangumi.org' + link_

    title_elem = elem.text
    content = content + '<p><a href="' + link + '">' + title_elem + '</a></p>\n'

# 記事を更新する
post_article(ARTICLE_ID, content)
