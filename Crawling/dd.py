from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://sports.daum.net/record/epl')
res = urlopen(req)

bs = BeautifulSoup(res, 'html.parser')
tags = bs.findAll('div', attrs={'class': 'inner_table'})
print(bs)
for tag in tags :
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
    print(tag.a.text)