import os
import re
import sys
from textXGrammar import execute as ex
from textXGrammar import unionrentacar as rc
from bs4 import BeautifulSoup


query_set = ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)
if isinstance(query_set, dict):
    query_set = {k: str(v) for k, v in query_set.items()}

if(type(query_set) == str):
    sys.exit(query_set)

html_response = rc.make_requests(query_set)
html_response = str(html_response)
html = html_response[2:len(html_response)-1]
#radi provere
print(html)

soup = BeautifulSoup(html, "html.parser")

#pronalazimo sve cene automobila
price_list_html = soup.find_all("div", class_="price_container")
price_list = []
price_per_day_list = []
#price_list_html = soup.find_all("span", class_="standard_price")
for price in price_list_html:
    children = price.find_all('p')
    for p in children:
        span = p.find_all('span')
        for s in span:
            if s['class'][0] == 'action_price':
                if len(s['class']) == 2:
                    #print('action_price price_per_day')
                    price = s.text
                    price = re.findall("\d+\,\d+", price)
                    price_per_day_list.append(price[0])
                else:
                    #print('action_price')
                    price = price.text
                    price = re.findall("\d+\,\d+", price)
                    price_list.append(price[1])
            if s['class'][0] == 'standard_price':
                if len(s['class']) == 2:
                    #print('standard_price price_per_day')
                    price = s.text
                    price = re.findall("\d+\,\d+", price)
                    price_per_day_list.append(price[0])
                else:
                    #print('standard_price')
                    price = price.text
                    price = re.findall("\d+\,\d+", price)
                    price_list.append(price[0])


'''for price in price_list_html:
    price = price.text
    price = re.findall("\d+\,\d+", price)
    price_list.append(price[0])
price_sum = price_list[::2]
#print(price_sum)
price_per_day = price_list[1::2]
#print(price_list[1::2])'''

#pronalazimo nazive(marke) automobila
cars_list_html = soup.find_all("h2", {"itemprop": "name"})

cars_list = []
i = 0
for car in cars_list_html:
    children = car.find_all("a", {"itemprop": "url"})
    for child in children:
        child = child.text
        cars_list.append(child)
        #print('jbmliti')
        #print(cars_list[i])
        i = i + 1

result_list_len = len(cars_list)
if(result_list_len<5):
    car_list_test = cars_list[:len(cars_list)]
    #print(car_list_test)
    price_list_test = price_list[:len(price_list)]
    #print(price_list_test)
    price_per_day_test = price_per_day_list[:len(price_per_day_list)]
    #print(price_per_day_test)
else:
    car_list_test = cars_list[:5]
    #print(car_list_test)
    price_list_test = price_list[:5]
    price_per_day_test = price_per_day_list[:5]

length = len(price_list_test) - 1
sorted = False

while not sorted:
    sorted = True
    for i in range(length):
        if price_list_test[i] > price_list_test[i+1]:
            sorted = False
            price_list_test[i], price_list_test[i+1] = price_list_test[i+1], price_list_test[i]
            price_per_day_test[i], price_per_day_test[i+1] = price_per_day_test[i+1], price_per_day_test[i]
            car_list_test[i], car_list_test[i+1] = car_list_test[i+1], car_list_test[i]

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
    if len(car_list_test) == 0:
        a = "Nema rezultata pretrage za unete kriterijume."
    else:
        a = test(car_list_test, price_list_test, price_per_day_test)
    f.write(a)