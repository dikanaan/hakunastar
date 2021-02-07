import requests, os
from requests.structures import CaseInsensitiveDict

url = "https://api.hakuna.live/login/facebook/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data={"facebookId":239360371088513,"accessToken":"EAAEBTh77bPkBAGpuhFAqLZA7RjOYDsp4y3Ov1dpXu9CQUc8nhjVZAJfvKsZBrNGaB8ZA42XRkFRrKBcV6OTWZCWpvXI8Fy57cKiZB1pQyOE1FBEYjll9y1VpEUZBevZCn8KlAxJYKXOdjYXT50KYi281Af3izDKH5bl8soYDnlvqJxNS16KrqC03zLDGI2fK14iCtGo1V3ChZBkMYreCtoOpF9KU5rxZAc5NPZCkS6nIp5NPw90lCUIReql","countryCode":"ID","timeZoneId":"Asia/Jakarta","region":"null","reactivate":"false"}
resp = requests.post(url, headers=headers, json=data)
bear = resp.json()['token']

print('')
link = input('Masukan link : ')
resp = requests.get(link)
respp = resp.url
linkt = respp[68:]
print('loading..')

url = "https://api.hakuna.live/v1/live-room/hosts/"+linkt

headers = CaseInsensitiveDict()
headers["accept-language"] = "in-ID"
headers["user-agent"] = "Hakuna/110 Android/6.0/443 okhttp/4.8.0"
headers["accept-encoding"] = "gzip"
headers["Authorization"] = "Bearer "+bear


resp = requests.get(url, headers=headers)

#print(resp.json())
roomid = resp.json()['roomId']

os.system('clear')


url = "https://api.hakuna.live/login/facebook/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

idfb = open('idfb.txt','r').read().splitlines()

tknfb = open('tknfb.txt','r').read().splitlines()

print('Inject listener by aku baic')
print('')
print('Judul Room : '+resp.json()['name'])
print('Host       : '+resp.json()['hostDisplayName'])
print('')
print('Max : '+str(len(idfb)))
stop = int(input('Jumlah : '))
for item in range(0, stop):
  reqq = requests.Session()
  data={"facebookId":idfb[item],"accessToken":tknfb[item],"countryCode":"ID","timeZoneId":"Asia/Jakarta","region":"null","reactivate":"false"}
  resp = reqq.post(url, headers=headers, json=data)

  #print(resp.json()['token'])
  bearer = resp.json()['token']
  #print(bearer)
  urlj = "https://api.hakuna.live/v2/live-rooms/"+str(roomid)+"/enter"
  urlp = "https://api.hakuna.live/v1/live-room/"+str(roomid)+"/participants"

  headers = CaseInsensitiveDict()
  headers["accept-language"] = "in-ID"
  headers["user-agent"] = "Hakuna/110 Android/6.0/443 okhttp/4.8.0"
  headers["Content-Type"] = "application/json"
  headers["Content-Length"] = "0"
  headers["accept-encoding"] = "gzip"
  headers["Authorization"] = "Bearer "+bearer
  
  respn = requests.post(urlj, headers=headers)
  
  print(respn.status_code)
  
  data1 = '{"cursor":null,"maxListLen":null}'
  resp1 = requests.post(urlp, headers=headers, data=data1)
  idpart = resp1.json()['participants'][0]['participantId']
  
  resp2 = requests.post("https://api.hakuna.live/v1/live-room/"+str(roomid)+"/participants/"+idpart+"/free-star", headers=headers)
  
  print(resp2)

os.system('python main.py')
