import requests
from bs4 import BeautifulSoup

def search_joongang_news():
    search = input()
    URL = f"https://www.joongang.co.kr/search/news?keyword={search}"
    return URL

def extract_new(html):
    news_title = html.find("a").get_text(strip=True).strip('\n')
    news_url = html.find("a")['href']
    return {
        'news_title':news_title,
        'news_url':news_url
    }
    
def extract_joongang_news(URL):
    cards = []
    res = requests.get(URL)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    news = soup.find("ul", {"class":"story_list"}).find_all("h2", {"class":"headline"})
    for new in news:
        card = extract_new(new)
        cards.append(card)
    return cards