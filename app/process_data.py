import json
import http.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_data(query_string):
    conn = http.client.HTTPSConnection('api.coinmarketcap.com')
    conn.request("GET", "{}".format(query_string))
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode('utf-8'))


def process():
    data = get_data('/v1/ticker/bitcoin/')
    return data[0]


def process_coins():
    data = get_data('/v1/ticker/?limit=10')
    return data
