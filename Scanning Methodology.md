
### Oracle Attack Methodology

```

1: "GET / HTTP/1.0" 
2: "GET / HTTP/1.1" 
3: "HEAD / HTTP/1.1"

curl -I example.com
curl --head  --url x.x.x.x
curl -X OPTIONS -Ix.x.x.x
curl -vX HEAD x.x.x.x
use auxiliary/gather/f5_bigip_cookie_disclosure
wafw00f meet.kbzbank.com
curl -v -X TRACE http://www.commercefun.com
curl -v -X OPTIONS http://www.commercefun.com
curl -v -X HEAD http://www.commercefun.com
curl -v -X GET http://www.commercefun.com
curl -v -X POST http://www.commercefun.com/secret
curl -v -X GET http://www.commercefun.com/secret



nmap --script http-robtex-reverse-ip secore.info
nmap -Pn -p80 --script=http-headers strategicsec.com
nmap -sS -sU -PN -p 1-65535 192.168.0.164(TCP SYN and UDP)
nmap --script http-methods
nmap -p 80 --script dns-brute.nse 
nmap --script http-enum
nmap -Pn -p80 --script=http-headers x.x.x.x

DNS Recon and MX Record

nslookup -query=mx redhat.com
nslookup -type=ns redhat.com
nslookup -type=soa redhat.com
nslookup -type=any google.com
Using Specific DNS server
nslookup redhat.com ns1.redhat.com
nslookup -port 56 redhat.com
nslookup -debug redhat.com
whois domain-name-here.com
Perform DNS IP Lookup (dig a domain-name-here.com @nameserver )
Perform MX Record Lookup (dig mx domain-name-here.com @nameserver)
Perform Zone Transfer with DIG(dig axfr domain-name-here.com @nameserver)
dig 1.1.1.1 -t any
dig 1.1.1.1 -t mx
dig 1.1.1.1 -t axfr
dig -x 1.1.1.1

dnsrecon -d 1.1.1.1
dnsenum nintendo.com
host -t ns megacorpone.com
host -t mx megacorpone.com
host idontexist.megacorpone.com
```



