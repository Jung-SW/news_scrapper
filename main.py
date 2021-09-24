from news_scrapper import search_news, extract_news
from save_as_csv import save_as_file

joongang = extract_news(search_news())
save_as_file(joongang)