from joongang_scrapper import search_joongang_news, extract_joongang_news
from save_as_csv import save_as_file

joongang = extract_joongang_news(search_joongang_news())
save_as_file(joongang)