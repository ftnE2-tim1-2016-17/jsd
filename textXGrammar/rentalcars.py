import urllib.request


def make_requests(model):
    response = [None]
    if request_www_rentalcars_com(response, model):
        print(response[0].headers.get_content_charset())
        html_response = response[0].read()
        response[0].close()
        return html_response


def request_www_rentalcars_com(response, model):
    response[0] = None

    #try:
    req = urllib.request.Request(
        "http://www.rentalcars.com/SearchResults.do?enabler=&"
        "country=Srbija&"
        "doYear="+model["yearTo"]+"&"
        "city="+model["city"]+"&"
        "driverage=on&"
        "doFiltering=true&"
        "dropCity="+model["city"]+"&"
        "driversAge=30&"
        "filterTo=49&"
        "fromLocChoose=true&"
        "dropLocationName="+model["city"]+"+(Sva+podru%C4%8Dja)+&"
        "dropCountryCode=&"
        "doMinute="+model["minuteTo"]+"&"
        "countryCode=&"
        "puYear="+model["yearFrom"]+"&"
        "puSameAsDo=on&"
        "locationName="+model["city"]+"+(Sva+podru%C4%8Dja)+&"
        "puMinute="+model["minuteFrom"]+"&"
        "doDay="+model["dayTo"]+"&"
        "searchType=allareasgeosearch&"
        "filterFrom=0&"
        "puMonth="+model["monthFrom"]+"&"
        "dropLocation=-1&"
        "doHour="+model["hourTo"]+"&"
        "dropCountry=Srbija&"
        "puDay="+model["dayFrom"]+"&"
        "puHour="+model["hourFrom"]+"&"
        "location=-1&"
        "doMonth="+model["monthTo"]+"&"
        "filterCoordinates=44.820934%2c20.307441%3a44.820934%2c20.292169")

    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/56.0.2924.87 Safari/537.36")
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    req.add_header("Accept-Language", "en-US,en;q=0.8")
    req.add_header("Cookie",
                   "CONNECTIONID=1486380317370|as-378|32899; tj_seed=001d4704101321aee44c0282f073000000; "
                   "tj_cip_correlation_id=B549FFAECBC271A37A760E89B3E99B43; rv=1; "
                   "JSESSIONID=BA0BB8FFFB5DE4FC23AEB72F4ADA12A2.node245a; "
                   "JSESSIONID=BA0BB8FFFB5DE4FC23AEB72F4ADA12A2.node245a; "
                   "cps=1; __utmt=1; __utmt_m=1; __utmt_b=1; _dc_gtm_UA-64959032-1=1; _dc_gtm_UA-64959032-2=1; "
                   "dpso=%7B%22data%22%3A%22country%3DSrbija%26city%3DNovi%2520Sad%26locationId"
                   "%3D-1%26dropCountry%3DSrbija%26dropCity%3DNovi%2520Sad%26dropLocationId%3D-1"
                   "%22%2C%22other%22%3A%7B%7D%7D; search=eyJsZWFkaW5nX3ByaWNlIjozNjE5LjE0LCJsb2NhdGlvbklkIjoiLT"
                   "EiLCJkcm9wTG9jYXRpb25JZCI6Ii0xIiwiZG9EYXRlIjoxNDg2ODkzNjAwMDAwLCJjdXJyZW5jeSI6IkVVUiIsImNpdHl"
                   "JZCI6IjE3MTgxIiwicHVEYXRlIjoxNDg2NjM0NDAwMDAwLCJkcml2ZXJzQWdlIjoiMzAiLCJkcm9wQ2l0eUlkIjoiMTcxO"
                   "DEiLCJ0aW1lc3RhbXAiOjE0ODY0OTUwNjI4MjB9; _gat_UA-64959032-1=1; _gat_UA-64959032-2=1; "
                   "tj_track=YWRjYW1wOnVZQVRPU1hTVlNOcm5ienY0YnZ5Snd8YWRwbGF0OlMxMTIwMzg4MTQ5Mjh8YWZmaWxpYXRlQ29kZT"
                   "pnb29nbGV8bGFiZWw6cnMtdVlBVE9TWFNWU05ybmJ6djRidnlKd1MxMTIwMzg4MTQ5Mjh8; WRUID=987031514.197821641;"
                   " tj_conf=\"tj_pref_currency:EUR|tj_pref_lang:rs|tjcor:rs|\"; "
                   "tjex=eJxtzjESwjAMBMDH0DoZn3SSoyIF%2FIUf8P9JbDAOCYWanZs7vVZwcS4KEy8xP1eiKKbHrXlIJi1L%0Aokj8Uzime"
                   "1dBeOyaLbRn383RsuY9%2B1FUpY%2BGb6%2BKj7XWq0k9DmuWgf2qjt4fHf8elH5SSRpSrlkK%0Acc5WVV5%2B2AAgJkF%2F; "
                   "ADRUM_BTa=\"R:542|g:f1d842f2-8b34-4674-9681-e91b752ab4b6|n:rentalcars_934e5cf6-5803-43fc-9fd5"
                   "-bff3f000060d\"; __utma=54629544.409906284.1486483158.1486492173.1486492221.3; "
                   "__utmb=54629544.186.4.1486495072789; __utmc=54629544; "
                   "__utmz=54629544.1486492221.3.3.utmcsr=google|utmgclid=COrP1YXP_tECFUoW0wodYFcDdA|"
                   "utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); _ga=GA1.2.409906284.1486483158; "
                   "LPCKEY-6382459=d0376c2d-7b8a-4c41-901b-474f6db3e973b-8957%7Cnull%7Cnull%7C40; "
                   "LPVID=MzN2MwNGI1NzkxNGUzMzQ2; LPSID-6382459=eQBUp2iQTNe9UDUFfKaBDA; RT=s=1486495083652; "
                   "ADRUM=s=1486495083652&r=http%3A%2F%2Fwww.rentalcars.com%2FSearchResults.do%3F1497810888")

    response[0] = urllib.request.urlopen(req)

    '''except urllib.error.URLError as e:
        if not hasattr(e, "code"):
            return False
        response[0] = e
    except:
        return False'''

    return True
