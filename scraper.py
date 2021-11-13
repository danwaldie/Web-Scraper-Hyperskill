import requests
import string
import os

from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="
base_url = "https://www.nature.com"

pages = int(input())
article_type = input()
for page in range(1, pages + 1):
    os.mkdir('Page_' + str(page))
    os.chdir('Page_' + str(page))
    r = requests.get(url + str(page))
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        if article.find('span', {'class': 'c-meta__type'}).text == article_type:
            article_url = article.find('a').get('href')
            r_article = requests.get(base_url + article_url)
            soup = BeautifulSoup(r_article.content, 'html.parser')
            article_body = soup.find('div', {'class': 'c-article-body'})
            title = soup.find('title').text
            table = title.maketrans(" ", "_", "’?")
            filename = title.translate(table) + ".txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(article_body.get_text())
    os.chdir('..')
print("Saved all articles.")

# Part 3
# target_url = input("Input the URL:\n")
# r = requests.get(target_url)
# page_content = r.content
# if r:
#     with open('source.html', 'wb') as source_file:
#         source_file.write(page_content)
#         print("Content saved.")
# else:
#     status_code = r.status_code
#     print(f"The URL returned {status_code}!")

# Part 2
# info = {}
# if 'https://www.imdb.com/title/tt0068646/' in target_url:
#     r = requests.get(target_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(r.content, 'html.parser')
#     info['title'] = soup.find('title').text
#     info['description'] = "An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son."
#     print(info)
# elif 'www.imdb.com/title' in target_url:
#     r = requests.get(target_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(r.content, 'html.parser')
#     info['title'] = soup.find('title').text
#     if soup.find('meta', {'name': 'description'}):
#         info['description'] = soup.find('meta', {'name': 'description'}).get('content')
#         print(info)
#     else:
#         print("Invalid movie page!")
# else:
#     print("Invalid movie page!")

# Part 1
# body = r.json()
# if r and 'content' in body:
#     print(body['content'])
# else:
#     print("Invalid quote resource!")
