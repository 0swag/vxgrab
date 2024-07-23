import requests
from bs4 import BeautifulSoup
import os
import json
import sys
from random import randint
from time import sleep
from rgbprint import Color



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
            folder = data[0][1]['value']['value'].split('/')[-2]
            tdir+=f"/{folder}"
            tlink+=f"/{folder}"
            print(f"[{Color.yellow}*{Color.reset}] Found directory: {folder}")
            os.system(f"mkdir -p {main_path}{tlink.split('https://vx-underground.org/Papers')[-1].replace('%20', '_').replace(' ', '_')}")            
            print(f"[{Color.light_green}+{Color.reset}] Created directory: {Color.light_blue}{main_path}{tlink.split('https://vx-underground.org/Papers')[-1].replace('%20', '_')}{Color.reset}")
            findStuff(tlink.replace(' ', '%20'))
            os.chdir()
        except Exception as e:
            pass
    for file in soup.find_all('a'):
        href = file.get('href')
        if href.endswith('.pdf') or href.endswith('.PNG') or href.endswith('.png') or href.endswith('7z') or href.endswith('zip') or href.endswith('jpg') or href.endswith('jpeg') or href.endswith('.txt'):
            savedir = f"{main_path}{link.split('https://vx-underground.org/Papers')[-1].replace('%20', '_')}"
            pdf_found+=1
            name = href.split('/')[-1]
            print(f"[{Color.yellow}*{Color.reset}] Found: {Color.light_blue}{name}{Color.reset}")
            resp = requests.get(href)
            print(f"[{Color.yellow}*{Color.reset}] Attempting to save in {Color.light_blue}{savedir}/{name}{Color.reset}")
            svdir = f"{savedir}/{name}/"
            #with open(f'{svdir}', 'wb') as fl:
            #fl.write(resp.content)
            treplace = r'/ '
            if os.path.exists(f"{savedir}/{name}"):
                print("File already exists")
            else:
                cmd = f"curl --silent \"{href.replace(' ', '%20')}\" -o \"{savedir}/{name}\""
                os.system(f"mkdir -p {savedir.replace(' ', '_')}")
                os.system(cmd)
                print(f"[{Color.light_green}+{Color.reset}] {Color.light_green}#{pdf_found}{Color.reset} Added: {Color.light_blue}{savedir}/{name}{Color.reset}")
                #sleep(3)

if len(sys.argv) < 2:
    print(f"[{Color.red}!{Color.reset}] Incorrect usage:\n %s <link> <destination>" % sys.argv[0])
    sys.exit()
link = sys.argv[1]
main_path = sys.argv[2]
findStuff(link)
