
### Useful Tshark and Tcpdump
```
#DNS query and the response address.
tshark -i wlan0 -f "src port 53" -n -T fields -e dns.qry.name 

# source / destination IP addresses
tshark -i wlan0 -f "src port 53" -n -T fields -e frame.time -e ip.src -e ip.dst -e dns.qry.name

```

```
#Dump HTTP request ASCII characters with TCPDUMP
tcpdump -nni eth0 -A port 80 and 'tcp[13] & 8!=0'

#Dump HTTP response ASCII information
tcpdump -nni eth0 -A src port 80

tcpdump -s0 -X dst port 80

tshark -i eth0-Y http.request -T fields -e http.host -e http.user_agent
```
