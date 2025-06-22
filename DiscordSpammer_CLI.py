import requests
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)

#notes
#fixed times error have no default value 
#deleted unused lab "datetime"
#added update system

def colors():
    global red, white, lightBlue, blue, reset, green, bright
    red = Fore.RED
    white=Fore.WHITE
    green=Fore.GREEN
    blue =Fore.BLUE
    bright=Style.BRIGHT
    lightBlue=Fore.LIGHTBLUE_EX
    reset = Fore.RESET


colors()

def read_tokens(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f'Error! The file {file_path} was not found.')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []

def read_channel_ids(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f'Error! The file {file_path} was not found.')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []

def spOm(channel_ids, tokens, content, times):
    if not isinstance(times, int):
        print("you can't use float on that! times set to default as 5")
        times=5

    else:
        for i in range(times):
            try:
                for token in tokens:
                    for channel_id in channel_ids:
                        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
                        headers = {'Authorization': token}
                        payload = {'content': content}
                        response = requests.post(url, json=payload, headers=headers)
                        print(f'\t{reset}{green}Response: {response.status_code} Message Sent! from token:{white} {token}{green} to channel: {white} {channel_id}{reset}')
                        if response.status_code != 200:
                            print(f'\t{reset}{red}Failed to send message with token:{bright} {token} {red}to channel:{bright} {channel_id}{reset}')
            except KeyboardInterrupt:
                print(" ( ! ) Keyboard Interrupt, quitting!")

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def main():
    channel_ids = []
    while True:
        try:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print(lightBlue+"""

\t·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
\t██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
\t▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
\t██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
\t▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•      ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀ 0.2
\tStormTools
            """)
            print(blue+"\t1) Insert tokens   2) Import tokens list\n\t3) Set channel IDs 4) Start\n\t5) Exit  \t   6) About and usage\n\t7) times \t   8) current version & update"+reset)
            user = input(f"\n\t{lightBlue}:> "+white).strip()

            if user in ['exit', '5']:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif user=='7': # the reason why the input 7 is sat to first is the var "times" is been called in the input 4
                global times
                try:
                    times = input(f'\t{reset}{lightBlue}times :> {white}').strip()
                    times = int(times)
                    print(f'\t{green}( * ) times set to : '+str(times)+' ( * )'+reset)
                    time.sleep(4)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                except ValueError:
                    print(f"\t{red} ( ! ) int numbers only! ( ! ) {reset}")
                    time.sleep(4)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

            elif user == '1':
                token = input(f'\t{reset}{lightBlue}Token:> {white}').strip()
                with open('tokens.txt', 'a') as r:
                    r.write(token + '\n')
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            elif user == '2':
                path = input(f'\t{reset}{lightBlue}Token list path:>{white}').strip()
                name = 'token_list.txt'
                file_path = find(name, path)
                if file_path:
                    tokens = read_tokens(file_path)
                    with open('tokens.txt', 'w') as r:
                        r.write('\n'.join(tokens))
                
                else:
                    print(f'{red}\tError! File not found {green}(make sure the file is named token_list.txt){reset}')
                    time.sleep(4)
                    os.system('cls' if os.name == 'nt' else 'clear')

            elif user == '3':
                channel_id = input(f'\t{lightBlue}Channel ID:> {white}').strip()
                channel_ids.append(channel_id)
                os.system('cls' if os.name == 'nt' else 'clear')

            elif user == '4':
                if not channel_ids:
                    print(f'{red}\t( ! ) Please insert at least one channel ID! ( ! ){reset}')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                tokens = read_tokens('tokens.txt')
                if not tokens:
                    print(f'{red}\t( ! ) Please insert tokens! ( ! )')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                try:
                    if times:1+1
                except NameError:
                    print(f"\t{red}Error times is None!, forget to set it? its in option 7")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                
                user_confirm = input(f'{lightBlue}\tAre you sure you want to start? (y/n){lightBlue} :> {white}').strip().lower()
                if user_confirm in ['yes', 'y']:

                    content = input(f'\t{lightBlue}Spam message :>{white} ').strip()
                    print(f'\t{blue}----------------------\n\tTokens:')
                    print(f'\n\t\t{green}'.join(tokens)+reset)
                    print(f'\n\t{lightBlue}Channel IDs: {green}{", ".join(channel_ids)}{reset}')
                    print(f'\t{lightBlue}Spam content:{white} {content}{reset}')
                    time.sleep(1)
                    spOm(channel_ids, tokens, content, times)
                elif user_confirm in ['no', 'n']:
                    continue
                else:
                    print(f'\t{red}( ! ) Unknown option! ( ! ) {reset}')

            elif user== '5':
                exit()

            elif user == '6':
                try:
                    with open('how_to_use.txt', 'r') as f:
                        file = f.read()
                        print(file)
                except FileNotFoundError:
                    print(lightBlue+f'''
\tDiscord: .6_g   
\tHow to use the Discord Spam Tool:
                          
\t1. Ensure the accounts are joined to the intended server or group.
\t2. Insert the accounts' tokens or a list of tokens.
\t3. Enter your spam content (links, emojis, text).
\t4. Set the times (better use 5)
\t5. Send the spam messages.
   
\tNote: It is recommended to use a different IP address to avoid Discord disabling your accounts.

\tCommand-Line Interface (CLI) Version:
\t(!) you can add muti channel ids in option 3 (!)

\t1. Run the Discord Spam Tool CLI.
\t2. Provide the tokens as command-line arguments or in a file.
\t3. Input your spam content when prompted.
\t4. Execute the command to begin sending the spam messages.
   
\t commands
\t 1. cls  : clear the terminal
                          
\t{Fore.RED}Disclaimer:
\t@StormTools, do not misuse this tool. I do not take responsibility for any misuse.\n\t This tool is created for educational purposes only.
'''+reset)
        
            elif user =='8':
                url = "https://raw.githubusercontent.com/SStorm21/StormToolsUpdates-Versions/main/S-DMS"
                res = requests.get(url)

                if res.status_code == 200:
                    current_version="0.2"
                    version = res.text.strip()

                    print(f"\n\t{lightBlue}you're current version is {current_version}, the available version is {version}{reset}")
                    print(f"\t{red}Please visit my github or sourceforge to install the new updates links:{green} https://sourceforge.net/u/stowrm/profile , https://github.com/SStorm21 {reset}")
                
                else:
                    print(f"\t\n{red}connection failed, are you connected to internet?{reset}")
                    #time.sleep(3)
                    #os.system('cls' if os.name == 'nt' else 'clear')
                    #continue
                    
            elif user == 'cls':
                os.system('cls' if os.name == 'nt' else 'clear')


            else:
                print(f'\t{red}( ! ) Unknown option! ( ! ) {reset}')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

        except KeyboardInterrupt:
            print(f'\n{red}(!) KeyboardInterrupt, Quitting! {reset}')
            exit()

if __name__ == '__main__':
    main()
