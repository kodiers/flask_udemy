import json
import http.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_data():
    conn = http.client.HTTPSConnection('api.coinmarketcap.com')
    conn.request("GET", "/v1/ticker/bitcoin/")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode('utf-8'))


def process():
    data = get_data()
    return data[0]
