import os
import re
from textXGrammar import execute as ex
from textXGrammar import unionrentacar as rc
from bs4 import BeautifulSoup


query_set = ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)
if isinstance(query_set, dict):
    query_set = {k: str(v) for k, v in query_set.items()}

html_response = rc.make_requests(query_set)
html_response = str(html_response)
html = html_response[2:len(html_response)-1]
#radi provere
print(html)

soup = BeautifulSoup(html, "html.parser")

#pronalazimo sve cene automobila
price_list_html = soup.find_all("span", class_="standard_price")
price_list = []
for price in price_list_html:
    price = price.text
    price = re.findall("\d+\,\d+", price)
    price_list.append(price[0])
price_sum = price_list[::2]
print(price_sum)
price_per_day = price_list[1::2]
print(price_list[1::2])

#pronalazimo nazive(marke) automobila
cars_list_html = soup.find_all("h2", {"itemprop": "name"})

cars_list = []

for car in cars_list_html:
    children = car.find_all("a", {"itemprop": "url"})
    for child in children:
        child = child.text
        cars_list.append(child)

car_list_test = cars_list[:5]
print(car_list_test)
price_list_test = price_sum[:5]
price_per_day_test = price_per_day[:5]


def test(strList, strList1, strList2):
    string = ''
    string += '<html><head>' \
           '<meta charset="UTF-8"><meta name="viewport" content="width-device-width, initial-scale-1">' \
           '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">' \
           '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js">' \
           '</script><script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js">' \
           '</script></head><body><h2 align="center">Automobili sa najpovoljnijim cenama: </h2><br>'
    string += '<div class="container"><table class = "table table-condensed" border="1"><th>Automobil</th><th>Cena</th><th>Cena po danu</th>'
    for i in range(len(strList)):
        string += '<tr><td>'+strList[i]+'</td><td>'+strList1[i]+'&euro;'+'</td><td>'+strList2[i]+'&euro;'+'</td></tr>'
    string += '</table></div></body></html>'
    return string


with open('result.html', 'w') as f:
    a = test(car_list_test, price_list_test, price_per_day_test)
    f.write(a)