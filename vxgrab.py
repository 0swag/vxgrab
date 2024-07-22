import requests
from bs4 import BeautifulSoup
import os
import json
import sys
from random import randint
from time import sleep



def findStuff(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    rm = soup.find('div', {'id': 'directory-tree'})
    rm.extract()
    pdf_found = 0
    savedir = ""
    for nav in soup.find_all('nav'):
        nav.extract()
    for links in soup.find_all('div'):
        try:
            tlink = link
            tdir = main_path
            data = json.loads(links.get('phx-click'))
            folder = data[0][1]['value']['value'].split('/')[-2].replace(' ', '_')
            tdir+=f"/{folder}"
            tlink+=f"/{folder}"
            print(tlink)
            findStuff(tlink)
            os.makedirs(f"{main_path}{tlink.split('https://vx-underground.org/Papers')[-1]}", exist_ok=True)
            #os.chdir(tdir)
        except Exception as e:
            pass
    for file in soup.find_all('a'):
        href = file.get('href')
        if href.endswith('.pdf'):
            savedir = f"{main_path}{link.split('https://vx-underground.org/Papers')[-1]}"
            pdf_found+=1
            name = href.split('/')[-1]
            print(f"[*] Found: {name}")
            resp = requests.get(href)
            print(f"[*] Attempting to save in {savedir}/{name}")
            svdir = f"{savedir}/{name}/"
            #with open(f'{svdir}', 'wb') as fl:
            #fl.write(resp.content)
            cmd = f"curl \"{href.replace(' ', '%20')}\" -o \"{savedir}/{name}\""
            print(cmd)
            os.system(f"mkdir -p {savedir}")
            os.system(cmd)
            print(f"[+] #{pdf_found} Added: {savedir}/{name} ")
            sleep(randint(0,20))

if len(sys.argv) < 2:
    print("[!] Incorrect usage:\n %s <link> <destination>" % sys.argv[0])
    sys.exit()
link = sys.argv[1]
main_path = sys.argv[2]
findStuff(link)
