import requests
from bs4 import BeautifulSoup

def get_all_str():
    url = input("電話番号を取得するページのURLを入力してください:")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="lxml")

    # ページ上のテキストを全てリスト化して返す
    return soup.find("html").text.split()