import os
import re
from textXGrammar import execute as ex
from textXGrammar import rentalcars as rc
from bs4 import BeautifulSoup


query_set = ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)

'''
html_response = rc.make_requests(query_set)
html_response = str(html_response)
html = html_response[2:len(html_response)-1]
#radi provere
print(html)

soup = BeautifulSoup(html, "html.parser")

price_list_html = soup.find_all("span", class_="carResultRow_Price-now")
price_list = []
for price in price_list_html:
    price = price.text
    price = re.findall("\d+\,\d+", price)
    price_list.append(price[0])

cars_list_html = soup.find_all("td", class_="carResultRow_CarSpec")

cars_list = []

for car in cars_list_html:
    children = car.find_all("h2")
    for child in children:
        child = child.text
        child = child.split("\\")[0]
        cars_list.append(child)

car_list_test = []
car_list_test.append(cars_list[0][:len(cars_list[0])-1])
car_list_test.append(cars_list[1][:len(cars_list[1])-1])
car_list_test.append(cars_list[2][:len(cars_list[2])-1])
price_list_test = []
price_list_test.append(price_list[0][:len(price_list[0])-1])
price_list_test.append(price_list[1][:len(price_list[1])-1])
price_list_test.append(price_list[2][:len(price_list[2])-1])

def test(strList, strList1):
    str = ''
    str += '<html><head>' \
           '<meta charset="UTF-8"><meta name="viewport" content="width-device-width, initial-scale-1">' \
           '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">' \
           '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js">' \
           '</script><script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js">' \
           '</script></head><body><h2 align="center">Automobili sa najpovoljnijim cenama: </h2><br>'
    str += '<div class="container"><table class = "table table-condensed" border="1"><th>Automobil</th><th>Cena</th>'
    for i in range(len(strList)):
        str += '<tr><td>'+strList[i]+'</td><td>'+strList1[i]+'</td></tr>'
    str += '</table></div></body></html>'
    return str


with open('result.html', 'w') as f:
    a = test(car_list_test, price_list_test)
    f.write(a) '''





