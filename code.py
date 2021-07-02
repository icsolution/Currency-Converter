import requests

def request(currency):
    coin = requests.get(f'http://www.floatrates.com/daily/{currency}.json').json()
    rates = {key: value['rate'] for key, value in coin.items()}
    if currency not in cache:
        cache[currency] = rates

def exchange(currency_from, currency_to, amount):
    print('Checking the cache...')
    if currency_to in cache:
        rate = cache[currency_from][currency_to]
        print('Oh! It is in the cache!')
        print(f'You received {rate * amount:.2f} {currency_to.upper()}.')
    else:
        request(currency_to)
        rate = cache[currency_from][currency_to]
        print('Sorry, but it is not in the cache!')
        print(f'You received {rate * amount:.2f} {currency_to.upper()}.')

def main():
    global cache
    cache = dict()
    request('usd')
    request('eur')
    has = input().lower()
    request(has)
    while True:
        wants = input().lower()
        if wants:
            amount = int(input())
            exchange(has, wants, amount)
        else:
            break

main()
