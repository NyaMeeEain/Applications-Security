
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
