# MOODLE CHECKER
### FOR EDUCATIONAL PURPOSE ONLY
<br />
Basic Moddle Password Checker
<br />
<br />
Here's what MoodleChecker looks in action.

```
$ python checker.py accounts.txt

 ███▄ ▄███▓ ▒█████   ▒█████  ▓█████▄  ██▓    ▓█████  ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓██▒    ▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒██░  ██▒▒██░  ██▒░██   █▌▒██░    ▒███   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒██   ██░▒██   ██░░▓█▄   ▌▒██░    ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░ ████▓▒░░ ████▓▒░░▒████▓ ░██████▒░▒████▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░   ░ ░      ░   ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
       ░       ░ ░      ░ ░     ░        ░  ░   ░  ░░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                              ░                     ░                       ░                               

Starting to check ...

Found working: tests:password
Found working: giveMeStar:Pls
Found working: Obviusly:IfYouWant

All accounts are already checked. Please check the hits file. Thanks for using this script ;)
```

## Setup

1) Clone the repository

```
$ git clone https://github.com/EverStarck/Moodle-account-checker
```

2) Install the dependencies

```
$ cd Moodle-account-checker
$ pip install -r requirements.txt
```

3) Introduce you login link and the check link

```python
url = "URL of the login page here"

checkIfLoginItem = "Url of some a tag that is only when you are in."
```


4) Run the script

```
$ python checker.py accounts.txt
```

## Compatibility

Tested on Python 3.9 on Linux and Windows. Feel free to open an issue if you have bug reports or questions. If you want to collaborate, you're welcome.


