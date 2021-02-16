# Pythonのお勉強 No.5 WordPressの自動更新
import requests
import urllib
from bs4 import BeautifulSoup

# スクレイピング対象
URL = 'https://www.tvkingdom.jp/'
KEYWORD = "香川真司 OR 久保建英"

# WordPress接続情報
WP_URL = 'xxxxxxxxxxxx'
WP_USERNAME = 'xxxxxxxxx'
WP_PASSWORD = 'xxxxxxxxxxx'

ARTICLE_ID = "9999"

# ニュース取得関数
def get_news(keyword):

    params = {'hl':'ja', 'gl':'JP', 'ceid':'JP:ja', 'q':keyword}

    # url、パラメータを設定してリクエストを送る
    res = requests.get(URL, params=params)
    print('ニュース取得結果:{}'.format(res))
    return res

# WordPress更新関数
def post_article(id, content):

    # REST APIを使うための認証情報
    user_ = WP_USERNAME
    pass_ = WP_PASSWORD
    # 更新情報
    payload = {"content": content}      #内容
               
    # 記事の更新を行う
    res = requests.post(urllib.parse.urljoin(WP_URL,  "wp-json/wp/v2/posts/817"),     #"wp-json/wp/v2/posts/<id>"にPostすると更新になる
                        json=payload,                                                   #投稿する記事の内容を設定する
                        auth=(user_, pass_))                                            #ユーザとアプリケーションパスワードを設定する
    print('WP投稿結果:{}'.format(res))
    return res

# メイン
article_no = 1
content = '香川真司と久保建英の最新ニュースです。'

res = get_news(KEYWORD)
soup = BeautifulSoup(res.content, "html.parser")

# レスポンスからh3階層のニュースを抽出する（classにxrnccdを含むタグ）
h3_blocks = soup.select(".xrnccd")

for i, h3_entry in enumerate(h3_blocks):

    # 記事を10件だけ処理する
    if article_no == 11:
        break
    
    # ニュースのリンクを抽出する（h3タグ配下のaタグのhref属性）
    link = h3_entry.select_one("h3 a")["href"]
    # 抽出したURLを整形して絶対パスを作る
    link = urllib.parse.urljoin(URL, link)

    content = content + '<p><a href="' + link + '">' + link + '</a></p>\n'
    article_no = article_no + 1

    # h3階層のニュースからh4階層のニュースを抽出する
    h4_block = h3_entry.select_one(".SbNwzf")

    if h4_block != None:
        # h4階層が存在するときのみニュースを抽出する
        h4_articles = h4_block.select("article")

        for j, h4_entry in enumerate(h4_articles):
            link = h4_entry.select_one("h4 a")["href"]
            link = urllib.parse.urljoin(URL, link)

            content = content + '<p><a href="' + link + '">' + link + '</a></p>\n'
            article_no = article_no + 1

# 記事を更新する
post_article(ARTICLE_ID, content)