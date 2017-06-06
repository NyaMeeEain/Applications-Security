
### Useful Tshark and Tcpdump
```
#DNS query and the response address.
tshark -i wlan0 -f "src port 53" -n -T fields -e dns.qry.name 

# source / destination IP addresses
tshark -i wlan0 -f "src port 53" -n -T fields -e frame.time -e ip.src -e ip.dst -e dns.qry.name

```
