import requests
import json

line = '212'
print('\n[n] northbound')
print('[s] southbound')
direction = input('\nWhich direction would you like your predictions for?: ')
direction = direction.upper()

# Ask user which direction they want predictions for. 
if direction == 'N':
    stop = '05200'
elif direction == 'S':
    stop = '13651'
else:
    print('You have entered an invalid command. Please try again.')

# Format URL to access predictions API
url = 'https://api.metro.net/agencies/lametro/stops/' + stop + '/predictions/'

# Get JSON data
data = json.loads(requests.get(url).text)

# print predictions

if direction == 'N':
    print('\nNorthbound line ' + line + ' at La Brea and Adams is predicted to arrive in: \n')
elif direction == 'S':
    print('\nSouthbound line ' + line + ' at La Brea and Adams is predicted to arrive in: \n')
else:
    print('\nAn unknown error has occured. \n')
for item in data['items']:
    print(item['minutes'])
