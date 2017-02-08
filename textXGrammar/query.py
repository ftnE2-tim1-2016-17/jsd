import os
import re
from textXGrammar import execute as ex
from textXGrammar import rentalcars as rc
from bs4 import BeautifulSoup


query_set = ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)

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
    str += '<html><head></head><body><h2>3 najjeftinia automobila</h2><br>'
    str += '<table border="1"><tr>'
    for i in strList:
        str += '<td>'+i+'</td>'
    str += '</tr><tr>'
    for j in strList1:
        str += '<td>'+j+'</td>'
    str += '</tr></table></body></html>'
    return str


with open('result.html', 'w') as f:
    a = test(car_list_test, price_list_test)
    f.write(a)





