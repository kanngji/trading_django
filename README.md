## 실행 방법

- cd trading_django
- python3 -m venv venv
- (왼도우 경우)
- source venv/Scripts/Activate (가상환경 실행)
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## DB 스키마

## 프로젝트 설계 구조

## 문제점 && 참고 URL

- 스크래핑을 해서 data를 긁어오는데 이게 요즘 불법이다.. 아니다 말이많아서 검색해본 도중에 robots.txt 에 대해서 알게됨
- robots.txt 파일이란
- https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt?hl=ko
- 여기에 잘 나와 있지만 쉽게 말해 User-agent에 대한 지침을 적어놓은 곳이다
- 많은 곳들이 User-Agent: \* 이 Disallow 되어 있지만 운이 좋게도 팍스넷에서 스크래핑하기도 쉬웠고 모든 user-agent에게
- allow 되어있어서 팍스넷에서 스크래핑을 했다. 스크래핑하는 라이브러리는 bs4 (BeautifulSoup)를 사용함
