# -*- coding: utf-8 -*-
import requests, ctypes, os, json
from colorama import Fore, init, Back, Style
from pystyle import *
init()

os.system('mode 80,24')
os.system('title ⚡️Discord Report Spammer ⚡️')
#----------------------------------------
nc = Fore.LIGHTGREEN_EX
rr = Fore.LIGHTRED_EX
clr = Back.LIGHTRED_EX
wht = Fore.LIGHTWHITE_EX
res = Style.RESET_ALL
niz = '\n\n\n\n\n\n\n'
xz = '\n\n\n\n\n\n\n\n\n\n\n                            '
logo = 'Discord Report Spammer'
git = f'{wht}                      https://github.com/Problematik1'
#----------------------------------------
print(f'{xz}{Fore.RED}{logo}')
print(f'{Fore.RED}{git}')
token = open("token.txt", "r").read().splitlines()
guild = input(f'\n{clr}{wht}Guild ID{res}{wht} > ')
channel = input(f'\n{clr}{wht}Channel ID{res}{wht} > ')
msg = input(f'\n{clr}{wht}Message ID{res}{wht} > ')

print(f'\n{rr}[{wht}1{rr}]{wht} Нелегальный контент')
print(f'{rr}[{wht}2{rr}]{wht} Домогательство')
print(f'{rr}[{wht}3{rr}]{wht} Спам или фишинг ссылки')
print(f'{rr}[{wht}4{rr}]{wht} Самоповреждение')
print(f'{rr}[{wht}5{rr}]{wht} NSFW-контент')
reason = input(f'\n{clr}{wht}Reason:{res}{wht} > ')
if reason == '1':
    reason = 0
elif reason == '2':
    reason = 1
elif reason == '3':
    reason = 2
elif reason == '4':
    reason = 3
elif reason == '5':
    reason = 4                

headers = {
 "Accept": "*/*",
 "Accept-Encoding": "gzip, deflate, br",
 "Accept-Language": "en-GB",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.42 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
 "Content-Type": "application/json",
 "Authorization": f"{token}"
        }
json = {"channel_id": channel, "message_id": msg, "guild_id": guild, "reason": reason}
url = 'https://discordapp.com/api/v9/report'



while True:
 r = requests.post(url, json = json, headers = headers)
 if r.status_code == 201:
     print(f'{nc} Success {r.text}')
 if r.status_code != 201:
     print(f'{rr} Error {r.text}')    
