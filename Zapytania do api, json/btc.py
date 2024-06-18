import json
import requests

page = 'https://api.coindesk.com/v1/bpi/currentprice.json'

resp = requests.get(page)

data = json.loads(resp.text)

date_btc=str(data['time']['updated'])

print(f'Notowania BTC w dniu {date_btc[:12]} o godzinie {date_btc[13:25]}')
print(f'1 BTC {str(data['bpi']['USD']['rate_float'])} USD')
print(f'1 BTC {str(data['bpi']['GBP']['rate_float'])} GBP')
print(f'1 BTC {str(data['bpi']['EUR']['rate_float'])} EUR')

with open('notowania_btc.txt', "a") as file:
    file.writelines(f'Notowania BTC w dniu {date_btc[:12]} o godzinie {date_btc[13:25]}\n')
    file.writelines(f'1 BTC {str(data['bpi']['USD']['rate_float'])} USD\n')
    file.writelines(f'1 BTC {str(data['bpi']['GBP']['rate_float'])} GBP\n')
    file.writelines(f'1 BTC {str(data['bpi']['EUR']['rate_float'])} EUR\n')
