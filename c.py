from fileinput import close
from lzma import FILTER_LZMA2
from os import stat
from pypresence import Presence
import time
import colorama
import os
import fade
import json


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def config_read():
    filename = "conf.config"
    contents = open(filename).read()
    config = eval(contents)
    pic = config['pic']


def menu2():
    filename = "conf.config"
    contents = open(filename).read()
    config = eval(contents)
    pic = config['pic']
    text = config['text']
    details = config['details']
    state = config['state']
    label = config['label']
    url = config['url']
    client_id = config['appid']
    
    RPC = Presence(client_id)
    RPC.connect()
    
    while 1:
        RPC.update(
            large_image= pic,
            large_text= text,
            details= details,
            state= state,
            start=int(time.time()),
            buttons=[{"label": label , "url": url}]
            #buttons= [{"label": "Take a look at the channel","url": "https://www.youtube.com/channel/UCseznP4Qb2DrRcDXcnAx_iw"}]
        )
        main()


def main():
    clear()
    print(f"[1] Exit")
    ans2 = input('> ')
    if ans2 == "1":
        print(f"Exiting...")
        time.sleep(2)
        os.system(exit())


def logo():
    colorama.deinit()
    os.system("mode con cols=135 lines=30")
    os.system("title Discord Rich Presence")
    clear()
    print(fade.pinkred(f'''
 _   _ _______  ___   _ ____        ____  ____   ____
| \ | | ____\ \/ / | | / ___|      |  _ \|  _ \ / ___|
|  \| |  _|  \  /| | | \___ \ _____| |_) | |_) | |
| |\  | |___ /  \| |_| |___) |_____|  _ <|  __/| |___
|_| \_|_____/_/\_\\___/|____/      |_| \_\_|    \____|             
'''))


if __name__ == '__main__':
    def menu():
        logo()
        print(f"[1] Start Discord RICH PRESENCE")
        print(f"[3] Exit")
        ans = input('> ')

        if ans == "1":
            menu2()
        elif ans == "2":
            print("[INFO] Exiting...")
            time.sleep(2)
            exit()
        else:
            print("[INFO] Invalid input! Exiting...")
            time.sleep(2)
            exit()

menu()
