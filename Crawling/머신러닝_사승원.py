from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# 2021.05.25, https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&league=100&tab=team, 사승원
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&league=100&tab=team')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.record_tbl > table > tbody > tr')
teamlist = []
for notice in notices:
    name = notice.select_one('.name').getText()
    rank = notice.select_one('.inner > strong').getText()
    match = notice.select('.inner')[2].select_one('span').getText()
    point = notice.select('.inner')[3].select_one('span').getText()
    win = notice.select('.inner')[4].select_one('span').getText()
    draw = notice.select('.inner')[5].select_one('span').getText()
    lose = notice.select('.inner')[6].select_one('span').getText()
    score = notice.select('.inner')[7].select_one('span').getText()
    lscore = notice.select('.inner')[8].select_one('span').getText()
    dif = notice.select('.inner')[9].select_one('span').getText()
    teamlist.append((name, rank, match, win, draw, lose, score, lscore, dif))
df = pd.DataFrame(teamlist)
df.to_excel('./eplTable.xlsx', index=False)