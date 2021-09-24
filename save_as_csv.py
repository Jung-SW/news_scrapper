import csv

def save_as_file(news):
    file = open("news.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["news_title", "news_URL"])
    for new in news:
        writer.writerow(list(new.values()))
    return