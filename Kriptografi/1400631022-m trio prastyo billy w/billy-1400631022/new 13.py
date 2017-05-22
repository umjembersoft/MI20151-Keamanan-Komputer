>>> from Crypto.Hash import SHA256
>>> from Crypto.PublicKey import RSA
>>> from Crypto import Random
>>> key = RSA.generate(1024, random_generator)
>>> text = 'abcdefgh'
>>> hash = SHA256.new(text).digest()
>>> hash
'\x9cV\xccQ\xb3t\xc3\xba\x18\x92\x10\xd5\xb6\xd4\xbfWy\r5\x1c\x96\xc4|\x02\x19\x0e\xcf\x1eC\x065\xab'
>>> signature = key.sign(hash, '')