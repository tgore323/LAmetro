import requests
from bs4 import BeautifulSoup
import csv
import json

line = '212'
print('\n[n] northbound')
print('[s] southbound')
direction = input('\nWhich direction would you like your predictions for?: ')

# Ask user which direction they want predictions for. 
if direction == 's':
    stop = '13651'
elif direction == 'n':
    stop = '05200'
else:
    print('You have entered an invalid command. Please try again.')

# Format URL to access predictions API
url = 'https://api.metro.net/agencies/lametro/stops/' + stop + '/predictions/'

# Get JSON data
data = json.loads(requests.get(url).text)

# print predictions

if direction == 'n':
    print('\nNorthbound line ' + line + ' predicted to arrive in: \n')
elif direction == 's':
    print('\nSouthbound line ' + line + ' predicted to arrive in: \n')
else:
    print('\nAn unknown error has occured. \n')
for item in data['items']:
    print(item['minutes'])


#data = json.loads(txt)
# Store data in text file
# txt_file = open('predict_data.json', 'w')
# txt_file.write(data)
# txt_file.close()

