import coinbasepro as cbp
import requests
from datetime import datetime

currentDate = datetime.today().strftime('%Y-%m-%d')

client = cbp.PublicClient()
cryptoSymbol = input("Enter crypto symbol:")
fiatCurrency = input("Enter fiat currency(EUR, USD, JPY, etc):")
info = client.get_product_ticker(cryptoSymbol+'-'+fiatCurrency)
print(info)
print(info.get("price"))


request = requests.get('https://api.pro.coinbase.com/products/' + cryptoSymbol+'-'+fiatCurrency +'/candles?start=2018-07-10T12:00:00&stop='+currentDate+'T12:00:00&granularity=900')
data = request.json()
counter = 0
for i in data:
    counter+=1
    print(counter, '$' + str(i[2]))
#print()
#currenciesDict = client.get_currencies()

#for i in range(len(currenciesDict)):
#    for key in currenciesDict[i]:
#        print(currenciesDict[i][key])
