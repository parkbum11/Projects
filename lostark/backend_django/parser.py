import requests
from bs4 import BeautifulSoup
import os

# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_django.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()

from user.models import LostarkData


def parser_user():
    # HTTP GET Request
    req = requests.get("https://www.inven.co.kr/board/lostark/4821/74101")
    # HTML 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, "html.parser")
    example = soup.select(
        "#tbArticle > div.articleMain > div.articleSubject > div.articleTitle > h1"
    )

    data = {}
    for title in example:
        data[title.text] = title.get("href")
    return data


if __name__ == "__main__":
    blog_data_dict = parser_user()
    for t, l in blog_data_dict.items():
        LostarkData(title=t, link=l).save()
