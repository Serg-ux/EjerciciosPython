import json
from urllib import request

moneda="bitcoin"
api_key = "b2668cd3e4f820172a995365c6085654"
unidades ="metric"

url = "ttps://api.blockchain.com/v3/exchange" % (moneda, unidades, api_key)
#print (url)

response = request.urlopen(url)

http_body = response.readline().decode('utf-8')

print (http_body)

#codificar la respuesta a json

data = json.loads(http_body)

#print(data)

#acceso al bloque main

main = data["main"]

#acceso a temperatura

temperatura = main["temp"]

#data = response.json()["main"]["temp"]

print ("La temperatura de " + ciudad + "es:" + str(temperatura))
