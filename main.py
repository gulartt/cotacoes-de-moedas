import requests
import json

data = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL");
data = data.json();

price_btc = data['BTCBRL'];
price_usd = data['USDBRL'];
price_eur = data['EURBRL'];

print("Qual cotação você quer conferir? ");
print("1 - BTC-BRL");
print("2 - USD-BRL");
print("3 - EUR-BRL");
option = input();

if(int(option) == 1):
    print('Cotação atual: {:.3f} R$'.format(float(price_btc['bid'])));
elif(int(option) == 2):
    print('Cotação atual: {:.2f} R$'.format(float(price_usd['bid'])));
elif(int(option) == 3):
    print('Cotação atual: {:.2f} R$'.format(float(price_eur['bid'])));
else:
    print("Opção inválida!!");