import requests
from bs4 import BeautifulSoup

def scrape():

url = "http://na.op.gg/champion/statistics"
r = requests.get(url)
r.content

soup = BeautifulSoup(r.content)

winrate = soup.find_all("div", {"class":"l-champion-index-content--side"})

for item in winrate:
  print item.contents[0].text

  scrape():
