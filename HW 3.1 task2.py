from collections import Counter
import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
root = tree.getroot()
items = root.findall(r'channel/item')


def find_words(file):
    words = list()
    for item in items:
        description = item[2].text
        for i in description.split():
            if len(i) >= 6:
                words.append(i)
    return words


def top_10():
    c = Counter(find_words(items))
    return c.most_common(10)


print(top_10())