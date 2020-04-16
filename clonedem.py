import requests
import json
import os

print('            #####################################')
print('            #                                   #')
print('            #  Clonedem                         #')
print('            #  version 1.0                      #')
print('            #  Author: Turrim                   #')
print('            #  https://owbird.github.io/Turrim  #')
print('            #                                   #')
print('            #####################################')

profile = input("[?] Enter profile: ")

print("\n[*] Gathering data...\n")

url = f"https://api.github.com/users/{profile}/repos"

res = requests.get(url)

data = json.loads(res.text)

db = {}

if ('message' in data):

    print(f"[!] Github profile {profile} does not exist")

    exit()

else:

    print(f"[+] Found {len(data)} repos\n")

for index, info in enumerate(data, 1):
    
    print(f"[+] {index}) Repository name: {info['name']}\n[+] Description: {info['description']}")
    
    print('-' * 15)

    db.setdefault(index, [info['name'], info['clone_url']])

download = int(input('[?] Enter repo number to download (0 to download all): '))

try:

    if download == 0:

        print(f"\n[*] Downloading all {len(data)} repos")

        for url in data:

        	print(f"[*] Downloading {url['name']}\n")

        	os.system(f"git clone {url['clone_url']}")

        	print(f"[+] Succefully downloaded {url['name']}\n")

    else:

        print(f"[*] Downloading {db[download][0]}")

        os.system(f"git clone {db[download][1]}")

        print(f"[+] Succefully downloaded {db[download][0]}")

except:

    print("[!] Download failed")

