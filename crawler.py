import urllib.request
from collections import Counter

import bs4 as bs
from nltk import word_tokenize

url1 = input("Enter a website to extract the URL's from: ")
url = "https://" + url1
tokens = []
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
visited_list = []
for para in soup.find_all('p'):
    l = para.text
    tokens += word_tokenize(l)
a = Counter(tokens)
final_tokens = []
for i in tokens:
    if i not in final_tokens:
        final_tokens.append(i)
frontier_list = []
for link in soup.find_all('a', href=True):
    s = link.get('href')
    if s.startswith('http'):
        if s not in frontier_list:
            frontier_list.append(s)

visited_list.append(url)
while frontier_list:
    url1 = frontier_list[0]
    frontier_list = frontier_list[1:]
    for a in visited_list:
        if a in url1:
            break
        else:
            tokens = []
            print(url1)
            # print(len(frontier_list))
            # print(len(visited_list))
            visited_list.append(frontier_list[0])
            sauce1 = urllib.request.urlopen(url1).read()
            soup = bs.BeautifulSoup(sauce1, 'lxml')
            for para in soup.find_all('p'):
                l = para.text
                tokens += word_tokenize(l)
            a = Counter(tokens)
            for i in tokens:
                if i not in final_tokens:
                    final_tokens.append(i)
            for link in soup.find_all('a', href=True):
                s = link.get('href')
                if s.startswith('http'):
                    if s not in frontier_list and s not in visited_list:
                        frontier_list.append(s)
        break
    if len(visited_list) > 5:
        break
# print(final_tokens)

x = input("Enter X")
y = input("Enter Y")

z = x + y

for l in final_tokens:
    if z in l:
        print(l)
    else:
        pass
