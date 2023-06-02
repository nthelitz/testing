import http.client

conn = http.client.HTTPSConnection("services.chanel.com")

payload = "division%5B%5D=1&division%5B%5D=2&division%5B%5D=5&division%5B%5D=3&productline%5B%5D=1&productline%5B%5D=2&productline%5B%5D=3&productline%5B%5D=4&productline%5B%5D=26&productline%5B%5D=5&productline%5B%5D=18&productline%5B%5D=19&productline%5B%5D=25&productline%5B%5D=10&productline%5B%5D=14&productline%5B%5D=13&productline%5B%5D=12&geocodeResults=%5B%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Br%C3%BCssel%22%2C%22short_name%22%3A%22Br%C3%BCssel%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Br%C3%BCssel%22%2C%22short_name%22%3A%22Br%C3%BCssel%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Belgien%22%2C%22short_name%22%3A%22BE%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Br%C3%BCssel%2C%20Belgien%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A50.7963456%2C%22west%22%3A4.3137683%2C%22north%22%3A50.9139024%2C%22east%22%3A4.437065899999999%7D%2C%22location%22%3A%7B%22lat%22%3A50.8476424%2C%22lng%22%3A4.3571696%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A50.7963456%2C%22west%22%3A4.3137683%2C%22north%22%3A50.9139024%2C%22east%22%3A4.437065899999999%7D%7D%2C%22place_id%22%3A%22ChIJZ2jHc-2kw0cRpwJzeGY6i8E%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Br%C3%BCssel%22%2C%22short_name%22%3A%22Br%C3%BCssel%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Belgien%22%2C%22short_name%22%3A%22BE%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Br%C3%BCssel%2C%20Belgien%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A50.763681%2C%22west%22%3A4.243765499999999%2C%22north%22%3A50.9139024%2C%22east%22%3A4.4822716%7D%2C%22location%22%3A%7B%22lat%22%3A50.8260453%2C%22lng%22%3A4.3802052%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A50.763681%2C%22west%22%3A4.243765499999999%2C%22north%22%3A50.9139024%2C%22east%22%3A4.4822716%7D%7D%2C%22place_id%22%3A%22ChIJ_58PdIbEw0cRMIBML6uZAAE%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%5D&iframe=true&logo=false&one_analytics=de&radius=26.181818181818183"

headers = {
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'x-requested-with': "XMLHttpRequest"
    }

conn.request("POST", "/de_DE/storelocator/getStoreList", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
