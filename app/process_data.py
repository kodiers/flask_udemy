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


def process(entered_coin):
    data = get_data('/v1/ticker/{}/'.format(entered_coin))
    return data[0]


def calculate_coin(price_usd):
    return float(price_usd) > 40


def process_coins():
    data = get_data('/v1/ticker/?limit=10')
    all_coins = []
    for coin in data:
        coin["isover40"] = calculate_coin(coin['price_usd'])
        all_coins.append(coin)
    return all_coins
