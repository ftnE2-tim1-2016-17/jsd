import urllib.request
import os
from textXGrammar import execute as ex


query_set = ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)
query_set = {k: str(v) for k, v in query_set.items()}
print(query_set)

def make_requests(model):
    response = [None]
    if request_www_unionrentacar_com(response, model):
        html_response = response[0].read()
        print(html_response)
        response[0].close()
        return html_response

cities = {
    "0": "0",
    "beograd": "3",
    "novi sad": "5",
    "nis": "3"
}
car_brands = {
    "0": "0",
    "alfa romeo": "30",
    "audi": "24",
    "bmw": "4",
    "chevrolet": "12",
    "citroen": "19",
    "dacia": "14",
    "fiat": "7",
    "ford": "26",
    "honda": "23",
    "hyundai": "21",
    "jaguar": "41",
    "jeep": "34",
    "kia": "33",
    "lancia": "31",
    "mazda": "39",
    "mercedes": "5",
    "nissan": "22",
    "opel": "16",
    "peugeot": "3",
    "renault": "6",
    "seat": "17",
    "skoda": "15",
    "suzuki": "25",
    "volkswagen": "18",
    "vw": "18",
    "volvo": "37"
}
fuel_types = {
    "0": "0",
    "benzin": "1",
    "plin": "8",
    "benzin plin": "8",
    "eurodizel": "9",
    "dizel": "2"
}
gearboxes = {
    "0": "0",
    "automatik": "5",
    "manuelni": "6",
    "poluautomatik": "7"
}
car_classes = {
    "0": "0",
    "gradski": "13",
    "niska klasa": "14",
    "srednja klasa": "15",
    "visoka klasa": "17",
    "luksuzni": "18",
    "skuter": "24",
    "limuzina": "25",
    "kombi": "26"
}


def request_www_unionrentacar_com(response, model):
    response[0] = None

    try:
        req = urllib.request.Request(
            "https://www.unionrentacar.com/search?"
            "pickup_town="+cities[model["city"]]+"&"
            "same_location=on&"
            "dropoff_town=0&"
            "dropoff_location=0&"
            "pickup_date="+model["dayFrom"]+"&"
            "pickup_month="+model["monthFrom"]+"."+model["yearFrom"]+"&"
            "pickup_hour="+model["hourFrom"]+"&"
            "pickup_minutes="+model["minuteFrom"]+"&"
            "dropoff_date="+model["dayTo"]+"&"
            "dropoff_month="+model["monthTo"]+"."+model["yearTo"]+"&"
            "dropoff_hour="+model["hourTo"]+"&"
            "dropoff_minutes="+model["minuteTo"]+"&"
            "car_brand="+car_brands[model["carBrand"]]+"&"
            "car_model=&"
            "fuel_type="+fuel_types[model["fuelType"]]+"&"
            "gearshift_type="+gearboxes[model["gearbox"]]+"&"
            "car_class%5B%5D="+car_classes[model["carClass"]]+"&"
            "price_from="+model["priceFrom"]+"&"
            "price_to="+model["priceTo"]+"&"
            "payway=0&"
            "deposit=0&"
            "mileage=0&"
            "search_submit=&"
            "action=search&"
            "sidebar_=sidebar_&"
            "advanced_search=1&"
            "puDay="+model["dayFrom"]+"&"
            "puMonth="+model["monthFrom"]+"&"
            "puYear="+model["yearFrom"]+"&"
            "doDay="+model["dayTo"]+"&"
            "doMonth="+model["monthTo"]+"&"
            "doYear="+model["yearTo"]+"&"
            "pickup_location=")

        req.add_header("Connection", "keep-alive")
        req.add_header("Upgrade-Insecure-Requests", "1")
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Referer", "https://www.unionrentacar.com/")
        req.add_header("Accept-Language", "en-US,en;q=0.8")
        req.add_header("Cookie", "sec_session_id=cc03f6bf695af9e6a70fb95b664d11ee; _ga=GA1.2.1018152463.1486482178")

        response[0] = urllib.request.urlopen(req)

    except urllib.error.URLError as e:
        if not hasattr(e, "code"):
            return False
        response[0] = e

    return True

make_requests(query_set)