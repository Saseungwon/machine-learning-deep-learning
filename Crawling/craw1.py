import bs4
import urllib.request

url = "https://sports.daum.net/record/epl"
html = urllib.request.urlopen(url)

o = bs4.BeautifulSoup(html, "html.parser")
l = (o.findAll("td", {"class":"inner_table"}))
print(l)

for i in l:
    print(i.find("span").text)