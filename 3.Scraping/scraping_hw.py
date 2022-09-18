import requests
import bs4


KEYWORDS = ['Искусственный интеллект', 'Транспорт', 'популяризация']
headers = {
    'Cookie': '_ym_d=1649583634; _ym_uid=1649583634769817403; _ga=GA1.2.1084108911.1649583634; hl=ru; fl=ru; visited_articles=570078:566004:570016:227377:664538:99923:196382; _ym_isad=2; habr_web_home_feed=/all/; _gid=GA1.2.1694905082.1660156609; pmtimesig=[[1660161479433,0],[1660162525508,1046075]]',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

url = 'https://habr.com/ru/all/'
response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_='tm-article-snippet')
art_list = []
for article in articles:
    art_date = article.find('time').attrs['title']
    article_tag_a = article.find('h2').find('a').text
    href = article.find('h2').find('a').attrs['href']
    link = 'https://habr.com' + href
    art_dict = {'date': art_date, 'title': article_tag_a, 'link': link}
    art_list.append(art_dict)

for article in art_list:
    response = requests.get(article['link'], headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    content = soup.find(class_="tm-article-presenter__content tm-article-presenter__content_narrow")
    for keyword in KEYWORDS:
        if keyword in content.text:
            print(article['date'], article['title'], article['link'])
