DOM based XSS vulnerabilities lies in client-side script.**Regularly DOM XSS is occurred when document object model is modified with attacker controllable part of the DOM** 
because The client-side scripts within an application's response take data from an attacker controllable part of the DOM.
```
<script> 
document.getElementsByTagName("Test")[0].innerHTML = "Test";
</script>
```

```
<script> 
var links = document.getElementsByTagName("a");
for (i=0; i < links.length; i++)
{
    links.[i].href = "http://192.168.100.100:9090/test.txt";
}
</script>
```

```
<script>
function CaughtClick()
{
    location.href = "http://192.168.100.100:9090/test.txt";
}
document.body.addEventListener('click', CaughtClick, true);
</script>
```
# The Value of Context is replaced by Executable XXS.
```
<script>
	var pos=document.URL.indexOf("context=")+8;
	document.write(document.URL.substring(pos,document.URL.length));
</script>
```
