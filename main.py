from src.timeklis import apstrada_datni, apstrada_lapu
from pprint import pprint
import re


# html = apstrada_datni("dati/piemers.html")

#pprint(html.head.title.text)
#pprint(html.body.h2)
#pprint(html.body.p)
#pprint(html.find_all('p'))
#pprint(html.find_all(id=True))
#pprint(html.find_all(id="viens"))
#pprint(html.find_all("p", class_="teksts"))

html = apstrada_lapu("https://www.tvnet.lv")
pprint(html.head.title.text)
raksti = html.find_all('a', class_="list-article__url")
print(len(raksti))
raksti = html.find_all('a', class_="list-article__url", string=re.compile("Latv"))
for r in raksti:
    print(r.text)
