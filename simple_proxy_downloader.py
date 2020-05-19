#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from colorama import Fore , init , Back
init(autoreset=False)

print(Fore.LIGHTRED_EX + """ 
┌─────────────────────────────────────────────┐
│              *** Proxy ***                  │ 
├─────────────────────────────────────────────┤
│       Gelistirilme Asamasındadır            │
│          + Eklenicek                        │
│          + Eklenicek                        │
│          + Eklenicek                        │
│          + Eklenicek                        │
├─────────────────────────────────────────────┤
│ Link: https://github.com/mrhacker51         │             
└─────────────────────────────────────────────┘
""")

def get_proxy_address():
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all"
    r = requests.get(url)
    return r

answered = get_proxy_address()

def proxy_address_registery():
    try:
        with open("proxies.txt","w") as proxy:
            if answered.status_code == 200:
                beautiful_proxy = BeautifulSoup(answered.content,"html.parser")
                proxy.write(str(beautiful_proxy))
                full_proxies_number = len(open("proxies.txt").readlines())
                print(Fore.CYAN +"İslem Basarili")
                print(Fore.YELLOW + str(full_proxies_number) + " " +"Adet Proxy Adresi Bulunmustur")
            else:
                print(Fore.GREEN + "Website Aktif Degildir !")
                quit()
    except:
        print("Error!!!")

proxy_address_registery()
