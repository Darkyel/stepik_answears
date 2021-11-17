/step/2

import requests

http_url = ''
alltext = []
count = 0
with open('C:\\Users\\igors\\Downloads\\dataset_3378_2.txt', 'r') as urlfile:
    for line in urlfile:
        line = line.strip()
        http_url = line
r = requests.get(http_url)
alltext = r.text.splitlines()
for i in range(len(alltext)):
    count += 1
print(count)

/step/3

import requests
import os

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('C:\\Users\\igors\\Downloads\\dataset_3378_3.txt', 'r') as urlfile:
    for line in urlfile:
        line = line.strip()
        if line.find('We') == -1:
            r = requests.get(line)
            line = r.text
        while line.find('We') == -1:
            newurl = os.path.join(url, line)
            r = requests.get(newurl)
            line = r.text
print(line)
