```
cat list.txt
https://github.com/NyaMeeEain
```
```

for i in $(cat list.txt); do data=$(curl -A "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)" -L -I -s -k  "{$i}") ; echo "URL: $i" >> output.txt ; echo "$data" >> output.txt ; done
cat output.txt | grep -o '<a .*href=.*>' | sed -e 's/<a /\n<a /g' | sed -e 's/<a .*href=['"'"'"]//' -e 's/["'"'"'].*$//' -e '/^$/ d'
cat output.txt | tr '"' '\n' | tr "'" '\n' | grep -e '^https://' -e '^http://' -e'^//' | sort | uniq
```
```
root@kali:~# cat list.txt
192.168.1.1
192.168.1.107
192.168.1.111
192.168.1.122
192.168.1.125
192.168.1.131
192.168.1.147
192.168.1.103

 for urt in $(cat list.txt); do nmblookup -A $urt; done
 for urt in $(cat list.txt); do smbclient -U '' -N -L //$urt; done
```
