```
cat list.txt
https://github.com/NyaMeeEain
```
```

for i in $(cat list.txt); do data=$(curl -A "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)" -L -I -s -k  "{$i}") ; echo "URL: $i" >> output.txt ; echo "$data" >> output.txt ; done
cat output.txt | grep -o '<a .*href=.*>' | sed -e 's/<a /\n<a /g' | sed -e 's/<a .*href=['"'"'"]//' -e 's/["'"'"'].*$//' -e '/^$/ d'
cat output.txt | tr '"' '\n' | tr "'" '\n' | grep -e '^https://' -e '^http://' -e'^//' | sort | uniq
```
