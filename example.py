import json
import requests
import datetime
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta

url = 'https://domdom.tistory.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

response = requests.get(url = url, headers = headers)

soup = BeautifulSoup(response.text, 'lxml')

boards = []
page = 1
loop = True
while loop:
    _url = url + '?page=' + str(page)
    # print(_url)
    res = requests.get(url = _url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')

    posts = soup.select('.post-item')
    now_date = datetime.datetime.now()
    before_two_month = now_date + relativedelta(months = -2)
    for post in posts:
        post_title = post.select_one('.title').text
        post_url = url + post.select_one('a').attrs.get('href')
        post_date = datetime.datetime.strptime(post.select_one('.date').text, '%Y. %m. %d.')

        if post_date < before_two_month:  # 현재 시점 2개월보다 더 지난 게시글이면 종료
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
    "before_two_month": str(before_two_month),
    "boards": boards
}
json_date = json.dumps(data)

with open('./two_month_latest_boards.json', 'w') as f:
    f.write(json_date)
