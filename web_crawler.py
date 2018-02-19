import requests
import re

to_crawl = ['http://azboost.com.br/']
crawled = set()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}
# força o navegamento pelo proxy
prox = {"http":"http://192.168.1.254:3128"}
while True:
    url = to_crawl[0]
    try:
        req = requests.get(url, headers=header,proxies=prox)
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    print 'Navegando:', url

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)