import time, requests
from colorama import Fore
from pystyle import Colors, Colorate
import os

def spamming_webhook():
    x=0
    y=0
    webhook_url=input(Fore.BLUE+"webhook url:> ")
    spam_content=input(Fore.BLUE+"spam content:> ")
    if webhook_url =="" or spam_content == "":
        print(Colorate.Horizontal(Colors.red_to_blue," ( x ) Error! webhook url or spam content is None! "));time.sleep(1)
        time.sleep(3)
        return

    else:
        while 1==1:
            
            data = {
                "content": str(spam_content),
                "username": "SStorm21 DSM 0.5",
                "avatar_url":"https://i.pinimg.com/1200x/c6/ab/b2/c6abb2cdcbee95f5f340896bf798f41a.jpg",
            }   
            response = requests.post(url=webhook_url, json=data)
            
            if response.status_code == 204:
                x+=1
                time.sleep(0.1);os.system('cls' if os.name == 'nt' else 'clear')
                print(Colorate.Horizontal(Colors.blue_to_cyan,"────[ WEBHOOK LOG ]───────────────────────"));print("")
                print(Colorate.Vertical(Colors.green_to_yellow,f"       ● SUCCESS {str(x)}"))
                print(Colorate.Vertical(Colors.red_to_green,f"       ● FAILURE {str(y)}\n\n"))

            else:
                y+=1
                
