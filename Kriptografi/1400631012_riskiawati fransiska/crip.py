from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
key
<_RSAobj @0x7f60cf1b57e8 n(1024),e,d,p,q,u,private>