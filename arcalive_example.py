import json
import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from dateutil.relativedelta import relativedelta

url = 'https://arca.live/b/gaijin'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url = url, headers = headers)

soup = BeautifulSoup(response.text, "html.parser")

"""print(response.text)"""

"""print(soup.text)"""

"""page = 1

for _page in range(1, 5):
    _url = url + "?p=" + str(_page)
    _response = requests.get(url = _url, headers = headers)
    _soup = BeautifulSoup(_response.text, "html.parser")
    print(_soup.text)"""


boards = []
page = 1
loop = True
current_date = datetime.datetime.now()

while loop:
    _url = url + "?p=" + str(page)
    # print(_url)
    res = requests.get(url = _url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    posts = soup.select(".list-table table")
    past_date = current_date + relativedelta(minutes = -30)

    for post in posts:
        post_title = post.select_one(".title").text
        post_url = url + post.select_one("a").attrs.get("href")
        post_date = datetime.datetime.strptime(post.select_one(".date").text, "%Y. %m. %d.")

        if post_date < past_date:   # 현재 시점보다 1개월 더 지난 게시글이면 종료
            loop = False
            # print(page, str(post_date), post_title)
            break

        board = {
            "title": post_title,
            "url": post_url,
            "date": str(post_date)
        }
        boards.append(board)

    page = page + 1

data = {
    "past_date": str(past_date),
    "boards": boards
}

json_date = json.dumps(data)

with open("./past_date_boards.json", "w") as f:
    f.write(json_date)

