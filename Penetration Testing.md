
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

### MSSQL

```
nmap -sU --script=ms-sql-info 192.168.1.108 192.168.1.156
auxiliary/scanner/mssql/mssql_ping
auxiliary/admin/mssql/mssql_enum
auxiliary/scanner/oracle/tnspoison_checker
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
```
