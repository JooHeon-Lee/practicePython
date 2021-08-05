# pypi 사이트 접속 ( 남들이 올린 패키지)
# pip list ==> 설치된 pip 리스트
# pip show 이름 ==> 설치한 pip 정보
# pip install -- upgrade 이름 ==> pip 업그레이드
# pip uninstall 이름 ==> pip 제거
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
