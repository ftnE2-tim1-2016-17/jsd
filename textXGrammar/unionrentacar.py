import urllib.request

def make_requests():
    response = [None]

    if request_www_unionrentacar_com(response):
        html_response = response[0].read()
        print(html_response)
        response[0].close()


def request_www_unionrentacar_com(response):
    response[0] = None

    try:
        req = urllib.request.Request("https://www.unionrentacar.com/search?pickup_town=0&same_location=on&dropoff_town=0&dropoff_location=0&pickup_date=06&pickup_month=03.2017&pickup_hour=18&pickup_minutes=30&dropoff_date=07&dropoff_month=03.2017&dropoff_hour=18&dropoff_minutes=30&car_brand=0&car_model=&fuel_type=0&gearshift_type=0&car_class%5B%5D=0&price_from=0&price_to=0&payway=0&deposit=0&mileage=0&search_submit=&action=search&sidebar_=sidebar_&advanced_search=0&puDay=06&puMonth=03&puYear=2017&doDay=07&doMonth=03&doYear=2017&pickup_location=")

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
    except:
        return False

    return True

make_requests()