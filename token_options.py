from tkinter import filedialog
import os
import shutil
from pystyle import Colors, Colorate
import time
from colorama import Fore
import requests

def import_token_list():
    global token_file_path

    try:
        print(Colorate.Horizontal(Colors.blue_to_cyan,"Importing Tokens List.."))
        tokens__ = filedialog.askopenfile(mode='r', filetypes=[('TXT Files', '*.txt')])
        if tokens__:
            token_file_path = os.path.abspath(tokens__.name)
            print(Colorate.Horizontal(Colors.blue_to_green,f"( + ) Tokens File Path --> {token_file_path}"))

            token_lines = [line.strip() for line in tokens__ if line.strip()]
            tokens__.close()
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if not token_lines:
                print(Colorate.Horizontal(Colors.red_to_blue," ( x ) This token file is empty!"))
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        
    except PermissionError:
        print("Permission denied.")

def import_channel_list():#ik its the same functions and i could use the define args but am too lazy for it rn :3
    global channel_file_path

    try:
        print(Colorate.Horizontal(Colors.blue_to_cyan,"Importing Channel List.."))
        channels_ids__ = filedialog.askopenfile(mode='r', filetypes=[('TXT Files', '*.txt')])
        if channels_ids__:
            channel_file_path = os.path.abspath(channels_ids__.name)
            print(Colorate.Horizontal(Colors.blue_to_green,f"( + ) Channel Ids File Path --> {channel_file_path}"))

            channel_id_lines = [line.strip() for line in channels_ids__ if line.strip()]
            channels_ids__.close()
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if not channel_id_lines:
                print(Colorate.Horizontal(Colors.red_to_blue," ( x ) This channel file is empty!"))
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        
    except PermissionError:
        print("Permission denied.")

def spam_token():
    spam_content=input(Fore.BLUE+"Spam Content:> ")
    
    fail = 0
    success = 0
    
    while 1:
        try:
            with open(token_file_path, 'r') as f:
                token = [line.rstrip() for line in f]
                for tokens in token:
                    with open(channel_file_path, 'r') as w:
                        channel = [line.rstrip() for line in w]
                        for channels in channel:
                            url = f'https://discord.com/api/v9/channels/{channels}/messages'
                            headers = {'Authorization': tokens}
                            payload = {'content': spam_content}
                            response = requests.post(url, json=payload, headers=headers)
                            if response.status_code == 204:
                                success+=1
                            time.sleep(0.1);os.system('cls' if os.name == 'nt' else 'clear')
                            print(Colorate.Horizontal(Colors.blue_to_cyan,"────[ TOKEN SPAM STATUS ]───────────────────────"));print("")
                            print(Colorate.Vertical(Colors.green_to_yellow,f"       ● SUCCESS {str(success)}"))
                            print(Colorate.Vertical(Colors.red_to_green,f"       ● FAILURE {str(fail)}\n\n"))
                            print(Colorate.Horizontal(Colors.blue_to_cyan,"────[ Channel IDs and Token Paths ]─────────────"));print("")
                            print(Colorate.Horizontal(Colors.blue_to_cyan,f" ❥・ Tokens File Path {token_file_path}\n ❥・ Channel ids File Path {channel_file_path}"));print("")

                            if response.status_code!=204:
                                fail+=1

                            else:
                                print(Colorate.Horizontal(Colors.red_to_yellow,f"( x ) Error! {response.status_code}!"))
                            
                                
                    
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear');print(Colorate.Horizontal(Colors.red_to_blue," ( x ) Keyboard Interrupt, quitting! "));exit()

        except NameError:
            print(Colorate.Horizontal(Colors.red_to_yellow,f"( x ) Error! U did not insert the Token or Channel lists! return.."))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return

    