import json
from collections import Counter


def find_words(file):
    words = list()
    for item in file['rss']['channel']['items']:
        text = item['description']
        for i in text.split():
            if len(i) >= 6:
                words.append(i.lower())
    return words


def top_10():
    c = Counter(find_words(news_json))
    return c.most_common(10)


with open('newsafr.json', encoding='utf-8') as f:
    news_json = json.load(f)
    print(top_10())
