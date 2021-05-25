import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://sports.news.naver.com/wfootball/record/index.nhn")
soup = BeautifulSoup(webpage.content, "html.parser")
result = soup.findAll("div", {"class":"record_tbl"})

print(result)