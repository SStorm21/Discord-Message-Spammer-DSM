import requests
import time,subprocess
import os
from tkinter import filedialog
import pyautogui, pyperclip, pyscreeze, winsound
from colorama import Fore, Style, init
from pyautogui import ImageNotFoundException
from datetime import datetime
import platform,getpass,os,sys
# Set frequency (Hz) and duration (milliseconds)
frequency = 250  # Example: 2500 Hz
duration = 1000   # Example: 1000 milliseconds (1 second)
image_found__=None
init(autoreset=True)
pyautogui.useImageNotFoundException()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def play(type):     
    global startup
    if type == "1":
        winsound.Beep(250, 200)#Startup
    elif type == "2":
        winsound.Beep(700, 250)#ErrorSound
    elif type == "3":
        winsound.Beep(500, 500)#Done
    elif type == "4":
        winsound.Beep(150, 20)#Select
    else:
        print("there is only 4 sounds ,idk what is that!")


    
def colors():
    global red, white, lightBlue, blue, reset, green, bright, MAGENTA
    red = Fore.RED
    white=Fore.WHITE
    green=Fore.GREEN
    blue =Fore.BLUE
    bright=Style.BRIGHT
    lightBlue=Fore.LIGHTBLUE_EX
    MAGENTA=Fore.MAGENTA
    reset = Fore.RESET

colors()
# in this version the tool is based on good cpu and weak cpu thats why i sat the timer btween most of things, ill change that in after 0.3 beta
# btw its build for windows cuz the last 71 donwloads was from windows users <3

def report(message): #will be added to 0.4 ? idk
    # get the webhook link from github
    # the info it will be taken from the user in exe version is : username - ip - system info ?
    # in the next update 0.4 the webhook spammer will be added and it will refuse to spam on report webhook and ban the user.

    
    pass

def read_tokens(file_path): #COLORS72
    try:
        with open(resource_path(file_path), 'r') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f'\t{red}( × ){blue} Error! The file {red}{file_path}{red} was not found.')
        return []
    except Exception as e:
        print(f'{blue}An error occurred:{red} {e}')
        return []

def read_channel_ids(file_path):#COLORS72
    try:
        with open(resource_path(file_path), 'r') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f'{red}( × ){blue}Error! The file {red}{file_path}{blue} was not found.')
        return []
    except Exception as e:
        print(f'{blue}An error occurred: {red}{e}')
        return []

def spOm(channel_ids, tokens, content, times):#COLORS72
    if not isinstance(times, int):
        print(f"{red}( × ){blue} you can't use float on that! times set to default as {green}5{blue}")
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
                        print(f'\t{reset}{green}( ✓ ) Response: {response.status_code} Message Sent! from token:{white} {token}{green} to channel: {white} {channel_id}{reset}')
                        if response.status_code != 200:
                            print(f'\t{reset}{red}( × ) Failed to send message with token:{bright} {token} {red}to channel:{bright} {channel_id}{reset}')
            except KeyboardInterrupt:
                print(" ( ( × ) ) Keyboard Interrupt, quitting!")

def friend_requests_(user_id_,tokens_list):#COLORS72
    for i in range(1):
        try:
            for token in tokens_list:
                time.sleep(2)
                url = f'https://discord.com/api/v10/users/@me/relationships/{user_id_}'
                headers = {
                    'Authorization': token,
                    'Content-Type': 'application/json'
                }

                response = requests.put(url, headers=headers, json={})

                if response.status_code == 204:
                    print(f"\n\t{green}( ✓ ) {blue}Friend request sent successfully! -->{red}{token}{reset}")
                elif response.status_code ==401:
                    print(f"\t{red}( × ) {blue}this token is vaild! --> {white}{token}{red} error code: {response.status_code} res: {response.text}")
                else:
                    print(f"\n\t{red}( × ) {blue}Failed to send friend request -->{token} {red} {response.status_code} - {response.text}{reset}")


        except KeyboardInterrupt:
            print(f" {blue}( {red}( × ){blue} ) Keyboard Interrupt, quitting!")

def find(name, path): #not used in 0.3
    for root, dirs, files in os.walk(resource_path(path)):
        if name in files:
            return os.path.join(root, name)
    return None

def read_token_file_path(file_path,name): #not used in 0.3 
    tokens = read_tokens(resource_path(file_path))
    with open('tokens.txt', 'w') as r:
        r.write('\n'.join(tokens))    

def load_tokens(file_path):
    with open(resource_path(file_path), 'r') as f:
        return [line.strip() for line in f if line.strip()]

def find_tokens_via_filedialoge(tool):
    print(f"\t{blue}Inserting token list ...")
    tokens__ = filedialog.askopenfile(mode='r', filetypes=[('TXT Files', '*.txt')])
    if tokens__:
        global token_file_path
        token_file_path = os.path.abspath(tokens__.name)
        print(f"\t{green}tokens file path --> {red}{token_file_path}")
        token_lines = [line.strip() for line in tokens__ if line.strip()]
        tokens__.close()
        if not token_lines:
            print(f"\t{red}( × ){blue} This token file is empty!, if this happen to you 1) the tool deleted the useless tokens from it 2) you just put an empty text file")
            main()
        elif tool =="freind_requests":
            friend_requests_(user_id_=user_id, tokens_list=token_lines)  
        elif tool == "automation_freind_requests":
            automation_freind_requests(user_name_or_id=user_id1,tokens=token_lines)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    
def look_for_the_image(image_name,huge_conf=None,error_message=None,found_message=None,found_error=None,click=None,write=None,username=None,exit=None,re_look=None):
    try: #keep the click method i will rewrite the whole code when it will be some 2.0 or smth
        
        if found_error == 1:
            look=pyautogui.locateOnScreen(resource_path(image_name),confidence=0.5)
            if look:
                print(found_message)
            else:
                pass
        elif click==1:
            image=pyautogui.locateOnScreen(resource_path(image_name),confidence=0.5)
            if image:
                pyautogui.click(image)
                if write==1:
                    pyautogui.write(username)
                else:
                        pass
            else:
                play(type=2)
                print(error_message)
                play(type=2)
        elif huge_conf==1:
            huge_conf=0.9
            pyautogui.locateOnScreen(resource_path(image_name),confidence=huge_conf)
        elif exit==1:
            quit()
        else:
            pyautogui.locateOnScreen(resource_path(image_name),confidence=0.2)

    except pyautogui.ImageNotFoundException:
        if re_look ==1:
            return 204 #a relook wid me to pass any relook methods on the same image
        elif error_message is None:
            print(error_message);quit()
        else:
            print(error_message);quit()

def find_image_click_on_it(Name):
    try:
        image=pyautogui.locateOnScreen(resource_path(Name),confidence=0.9)
        if image:
            pyautogui.click(image)
            return 1
    except pyautogui.ImageNotFoundException:
       # print("i can't find this image!")
        return 0

def automation_freind_requests(user_name_or_id,tokens): #COLORS72
    def send_friend_request(): #2
        pyautogui.hotkey("ctrl","shift","i");time.sleep(3)
        try:
            login_page=look_for_the_image(re_look=1,image_name=resource_path("login_screen.png"),found_message=f"\t{red}( × ) {blue}Token --> {red}{token}{blue} is vaild cuz it could not login to {lightBlue}discord{blue}!, trying with other tokens..",found_error=1)
            if login_page is None: #the login page was found witch means the token was not usable.
                play(type="2")
                file_path = r"{}".format(token_file_path) 
                pyautogui.hotkey("win","d") #mini all other windows 
                time.sleep(1.6)
                pyautogui.hotkey("win","r");pyautogui.write(f'notepad.exe "{file_path}"');pyautogui.press("enter")
                #os.system(f'start /max notepad.exe "{file_path}"')
                buttons=['pageup','end']
                time.sleep(2)
                for i in buttons:
                    pyautogui.press(i)
                for i in range(72):
                    pyautogui.press("backspace")
                buttons2=["down","backspace"]
                for i in buttons2:
                    time.sleep(2.5)
                    pyautogui.press(i)
                time.sleep(2.5)
                pyautogui.hotkey("ctrl","s");time.sleep(1);pyautogui.hotkey("alt","f4");time.sleep(1)
                look_for_the_image(image_name=resource_path("oprea icon.png"),click=1,error_message=f"\t{red}( × ){blue} i can't found opreaGx icon on you're screen, Please open it so we can continue the login function")#pyautogui.hotkey("win","shift","m")
                time.sleep(5)
                login_token()
#to to fix, thje porplem is the tool look for the login image and return no value after if, add a return value and set the function as a 
#global var like imagevalue set to 0 or 1 and make an if statemnt look for it and work based on it
            elif login_page == 204:
                print(f"\t{green}( ✓ ){blue} Token --> {green}{token}{blue} works! going to send the friend request..");time.sleep(4)
#change the token? reset password or logout
                #see the login via image? nah #logged_in=look_for_the_image(image_name="if_its_logged.png",found_message=f"\t{green}( ✓ ) {blue}Token --> {green}{token}{blue} works! going to send the friend request..",error_message="i can't find if_its_logged")

                #elif look_for_the_image is None:
                    #print(f"\t{blue}could not found discord login page, slow internet? .. trying")
                    #look_for_the_image(image_name="login_screen.png",found_message=f"\t{red}( × ){blue}Token --> {red}{token}{blue} is vaild cuz it could not login to {lightBlue}discord{blue}!, trying with other tokens..",found_error=1)
                add_friend=find_image_click_on_it(Name=resource_path("add_freind1.png"))
                if add_friend ==1:
                    print()
                    #look_for_the_image(image_name="add_freind1.png",error_message=f"\t{red}( × ){blue} could not found the add friend button",found_message=f"\t{green}( ✓ ){blue} friend button found!, going to add --> {user_name_or_id}",click=1)
                    search_user_name=find_image_click_on_it(Name=resource_path("search_user_name2.png"))
                    if search_user_name==1:
                        print(f"\t{green}( ✓ ){blue} search user found!, going to wrtie --> {user_name_or_id}")
                        pyautogui.write(user_name_or_id)
                        #look_for_the_image(image_name="search_user_name2.png",found_message=f"\t{green}( ✓ ){blue} search user found!, going to wrtie --> {user_name_or_id}",error_message=f"\t{red}( × ){blue} could not found the name button",click=1,username=user_name_or_id)
                        pyautogui.press('enter')
                        time.sleep(4)
                        #fr_request=look_for_the_image(huge_conf=1,image_name="closed_friend_request_proplem.png",found_error=1,found_message=f"\t{blue}The current user --> {white}{user_name_or_id}{red} closed{blue} the friend reuqests, there is no reason to use this option right now..")
                        fr_request=find_image_click_on_it(Name="closed_friend_request_proplem.png")
                        if fr_request==1:
                            print(f"\t{blue}The current user --> {white}{user_name_or_id}{red} closed{blue} the friend reuqests, there is no reason to use this option right now..");exit()
                            #now the user is been written, click on the add friend message and look if the user has locked his freind request func
                            #look_for_the_image(image_name="send_freind_request3.png",found_message=f"\t{green}( ✓ ){blue} send friend request button found, send to --> {user_name_or_id}",error_message=f"\t{red}( × ){blue} could not found add friend button!",click=1)
                            #if look_for_the_image:
                            #    #look_if_its_closed  see if the user closed the friend request or not
                            #    look_for_the_image(image_name="can't_send_friend_request4.png",found_message=f"\t{green}( × ){blue} this user closed his friend request --> {user_name_or_id}, there is no use to send friend reqeust to this account! exit.",exit=1)
                        elif fr_request ==0:
                            print(f"\t{green}( ✓ ){blue} send friend request found, has been sent to --> {user_name_or_id}, going to other tokens")
                            pyautogui.hotkey("ctrl","t"),pyautogui.hotkey("ctrl","shift","delete");time.sleep(1.5)
                            delte_history_etc=find_image_click_on_it(Name=resource_path("Delete.png"))
                            if delte_history_etc==1:
                                print(f"\t{blue}deleted the history cuz logging out will {red}disable{red} the {green}token{green}!");time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                pyautogui.hotkey("ctrl","l");pyautogui.write("https://discord.com/login");pyautogui.press("enter");login_token()
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                pyautogui.hotkey("ctrl","l");pyautogui.write("https://discord.com/login");pyautogui.press("enter");login_token()

                    else:
                        print(f"\t{red}( × ){blue} could not found the search username bar!");exit()
                else:
                    print(f"\t{red}( × ){blue} could not found the add friend button");exit()

        except Exception as e:
            print(e);exit()


    def login_token(): #1
        global token
        with open(token_file_path, 'r') as f: #reread the token file to see if it was updated
            tokens = [line.strip() for line in f if line.strip()]
        if not tokens:
            print(f"\t{red}No more tokens left in the file.")
        token = tokens[0]
        print(f"\t{blue}the tool will start please open the discord on web, {green}10s{blue} left");time.sleep(10)
        look_for_the_image(image_name=resource_path("LoginPage0.png"),error_message=f"\t{red}( × ) {blue}can't find discord login page, did you open it on browser?\n\t{blue}Exiting!",found_message=f"\t{green}( ✓ ){blue} login page found! starting the login method..")
        pyautogui.hotkey("ctrl","shift","j");time.sleep(2) #open the console and use tab to write on it
        time.sleep(5);pyautogui.typewrite("allow pasting");time.sleep(0.5);pyautogui.press("enter") #you might need to use Tab to enter the console instant
        for token in tokens:
            print(f"\t{blue}Username or ID: {white}{user_name_or_id}\n\t{blue}current token --> {lightBlue}{token}")
            command1="""
login = token => { setInterval(() => document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"${token}"`, 50); setTimeout(() => location.reload(), 2500); }; login(\""""+token+"""\");"""
            time.sleep(2);pyautogui.typewrite(command1);time.sleep(2);pyautogui.press("enter");time.sleep(9)
            send_friend_request()

    login_token()

def Update_section(type=None):
    def send_update_request(system_lookup=None):
        play(type="4")
        if system_lookup==1:
            url = "https://raw.githubusercontent.com/SStorm21/StormToolsUpdates-Versions/main/S-DMS"
            res = requests.get(url)

            if res.status_code == 200:
                current_version="0.3 beta"
                version = res.text.strip()
                if current_version == version:
                    pass
                else:
                    print(f"\n\t{blue}( ✓ ){lightBlue}you're current version is {current_version}, the available version is {version}{reset}")
                    print(f"\t{red}Please visit my github or sourceforge to install the new version links:{green} https://sourceforge.net/u/stowrm/profile , https://github.com/SStorm21 {reset}")
                    time.sleep(5)
            else:
                print(f"\t\n{red}( × ){blue} connection failed, are you connected to internet?{reset}");time.sleep(5)

        
    if type==1: #startup looking for update has a sleep for 5s and clear it 
        send_update_request(system_lookup=1)


    pass

def main():
    channel_ids = [] #\t\t{datetime.now()} / {platform.system()} {platform.version()} / {getpass.getuser()}
    while True:
        try:
            Update_section(type=1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(lightBlue+f"""

\t·{blue}▄▄▄▄{lightBlue}  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      {blue}.▄▄ ·{lightBlue}  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄ 
\t{blue}██▪ ██{lightBlue} ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     {blue}▐█ ▀.{lightBlue} ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
\t{blue}▐█· ▐█▌{lightBlue}▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    {blue}▄▀▀▀█▄{lightBlue} ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄
\t{blue}██. ██{lightBlue} ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     {blue}▐█▄▪▐█{lightBlue}▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
\t{blue}▀▀▀▀▀•{lightBlue} ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•      {blue}▀▀▀▀{lightBlue} .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀ 0.3 Beta
\t\t@StormTools Discord -> .p3hv {red}Tokens expire on logout and renew on login!{blue}
\t\t{lightBlue}join my discord: https://discord.gg/BZynQaFenU{blue}
\n\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀""")
            print(blue+f"""\n\tchannel options\n\t-----------------+\n\t1) insert tokens   2) import tokens list\n\t3) set channel IDs 4) times\n\t5) start 
\n\tusers options\n\t-----------------+\n\t6) send friend request{red} ( via API and you will get a captcha-required error so pass it ){blue}
\t7) send friend request via Browser\n\n\tcommands\n\t-----------------+\n\t/exit\n\t/usage"""+reset)
            play(type="1")
            user = input(f"\n\t{lightBlue}:> "+white).strip()
            if user in ['exit', '/exit']:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif user=='4': # the reason why the input 7 is sat to first is the var "times" is been called in the input 4
                global times
                try:
                    play(type="4")
                    times = input(f'\t{reset}{lightBlue}times :> {white}').strip()
                    times = int(times)
                    play(type="3");print(f'\t{green}( ? ) times set to : '+str(times)+' ( * )'+reset)
                    time.sleep(4)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                except ValueError:
                    play(type="2")
                    print(f"\t{blue}( {red}( × ){blue} ) int numbers only! ( {red}( × ){blue} ) {reset}")
                    time.sleep(4)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

            elif user == '1':
                play(type="4")
                token = input(f'\t{reset}{lightBlue}Token:> {white}').strip()
                with open('tokens.txt', 'a') as r:
                    r.write(token + '\n')
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            elif user == '2':
                play(type="4")
                path = input(f'\t{reset}{lightBlue}Token list path:>{white}').strip()
                name_ = 'tokens.txt'
                file_path = find(name_, path)
                if file_path:
                    read_token_file_path(file_path=path,name=name_);play(type="3")
                else:
                    play(type="2")
                    print(f'{red}\tError! File not found {green}(make sure the file is named tokens.txt){reset}')
                    time.sleep(7)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    

            elif user == '3':
                play(type="4")
                channel_id = input(f'\t{lightBlue}Channel ID:> {white}').strip()
                channel_ids.append(channel_id)
                os.system('cls' if os.name == 'nt' else 'clear')

            elif user == '5':
                play(type="4")
                if not channel_ids:
                    play(type="2");print(f'{red}\t( ! ) Please insert at least one channel ID! ( ! ){reset}')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                tokens = read_tokens('tokens.txt')
                if not tokens:
                    play(type="2")
                    print(f'{red}\t( ! ) Please insert tokens! ( ! )')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                try:
                    if times:1+1
                except NameError:
                    play(type="2")
                    print(f"\t{red}Error times is None!, forget to set it? its in option 7")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                
                user_confirm = input(f'{lightBlue}\tAre you sure you want to start? (y/n){lightBlue} :> {white}').strip().lower()
                if user_confirm in ['yes', 'y']:
                    play(type="3")
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
                    play(type="2")
                    print(f'\t{red}( ! ) Unknown option! ( ! ) {reset}')

            elif user == '/usage':
                play(type="4")
                try:
                    with open('how_to_use.txt', 'r') as f:
                        file = f.read()
                        print(file)
                except FileNotFoundError:
                    print(lightBlue+f'''
                
\tDiscord: .p3hv   
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
\t 2. exit : quit
\t{Fore.RED}Disclaimer:
\t@StormTools, do not misuse this tool. I do not take responsibility for any misuse.\n\t This tool is created for educational purposes only.
'''+reset)
            
            elif user=='6':
                play(type="4")
                global user_id
                user_id=input(f"\n\t{blue}user ID :> ")
                if user_id:
                    find_tokens_via_filedialoge(tool="freind_requests")
        
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            
            elif user=='7':
                play(type="4")
                global user_id1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""\n\t{blue}this option works like {white}\'OpenCV bot\'{blue} please follow the rules to make sure everything will be done right
\n\t1) open discord login page Link --> {white}https://discord.com/login{blue} on {white}google {green}chrome{blue} (Ash theme).
\t2) {red}make sure{blue} the keyboard is not set to {red}UpperCase{blue} and the language is set to english.
\t3) the browser{red} scale {blue}in this version used 100% with a 1920x1080 100% display scale and resolution .
\t4) use a VPN or something so discord wont take actions to you're real ip (better create new accounts via {MAGENTA}Tor{blue} using any onion email services if you don't have accounts for spamming)
\t5) {red}Dont{blue} touch anything let the tool do its job.
\t{red}NOTE: {blue}BASED ON CHROME AND IT WILL DELETE THE --> Browse history, cookies/site data, and cached images/files from the last hour.
""")

                user_id1=input(f"\n\t{blue}username :> {white}")
                if user_id1:
                    play(type="4")
                    find_tokens_via_filedialoge(tool="automation_freind_requests")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
            elif user == 'cls':
                os.system('cls' if os.name == 'nt' else 'clear')

            #elif user == '/report':
            #    msg = input("\t{green}report :>{red}")
            #   report(message=msg)
                
            else:
                play(type="2")
                print(f'\t{red}( × ) Unknown option! ( × ) {reset}');time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

        except KeyboardInterrupt:
            play(type="2");print(f'\n\t{red}( × ){green} KeyboardInterrupt, Quitting! {reset}')
            exit()

if __name__ == '__main__':
    main()
