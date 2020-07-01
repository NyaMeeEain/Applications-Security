#!/ust/bin/python
import readline
import requests
from bs4 import BeautifulSoup

cookie = { "Cookie": "PHPSESSID=1tmgthfok042dslt7lr7nbv4cb" }

while True:
    data_input = raw_input("> ")
    read = requests.get("http://pentesterlabXXXXX", cookie=cookie)
    soup = BeautifulSoup(read.text, 'html.parser')
    csrf = soup.find("input", {"name": "token"})["value"]
    data = { "username": "user", "password": "pass", "db": data_input, "token": csrf, "login": ""}
    print data
    read = requests.post("http://pentesterlabXXXXX", data=data, cookie=cookie)
    print read.text

