from pystyle import Colors, Colorate
import os
from colorama import *
from token_options import *
from user_options import *
from other_options import *

def main():
    while True:
        try:
            print(Colorate.Horizontal(Colors.blue_to_cyan,"""               
\t·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄ 
\t██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
\t▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄
\t██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
\t▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•      ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀ 0.5
\t\t@StormTools Discord -> .p3hv Tokens expire on logout and renew on login!
\n\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
\n\tToken Options
\t──────────────────
\t1 ) Import Tokens List
\t2 ) Import Channels List
\t3 ) Start Spamming

\tOther Options
\t──────────────────
\t4 ) Webhook Spammer
 
"""))
#\n\tUser Options
#\t──────────────────
#\t4 ) Spam Friend Request (via UI)

            user=input(Fore.BLUE+":> ")
            if user=="1":
                import_token_list()
                
            elif user=="2":
                import_channel_list()
                
            elif user=="3":
                spam_token()
                
            elif user=="4":
                spamming_webhook()
            
            #elif user=="4":
            #    spam_friend_requests_via_ui()
                
            else:
                print(Colorate.Horizontal(Colors.red_to_blue," ( x ) uknown option, return.. "));time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

            
        except KeyboardInterrupt:
            print(Colorate.Horizontal(Colors.red_to_blue," ( x ) Keyboard Interrupt, quitting! "));exit()

if __name__=="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()