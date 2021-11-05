import requests
import re

def main():
    save = ''
    positivo = 0
    negativo = 0

    r = requests.get(f'https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html')
    save += r.text
    pattern = ("[\w+-][0-9.]+\sBTC")
    r = re.findall(pattern, save)
    for x in r:
        if '-' in x:
            print(x)
            y = x.strip(' BTC')
            negativo += float(y)
        if '+' in x:
            print(x)
            y = x.strip(' BTC')
            positivo += float(y)
    print(f'Negativo: {negativo}')
    print(f'Positivo: {positivo}')

if __name__ == '__main__':
    main()
