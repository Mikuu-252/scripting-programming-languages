import json
import requests

page = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'

resp = requests.get(page)

data = json.loads(resp.text)

print('Population by year:')
with open('us-population.txt', 'w', encoding="UTF-8") as file:
    for year in data['data']:
        print(f'Year {year['Year']}: {year['Population']}')
        file.write(f'Year {year['Year']}: {year['Population']}\n')

