>>> from Crypto.Cipher import ARC4
>>> obj1 = ARC4.new('01234567')
>>> obj2 = ARC4.new('01234567')
>>> text = 'abcdefghijklmnop'
>>> cipher_text = obj1.encrypt(text)
>>> cipher_text
'\xf0\xb7\x90{#ABXY9\xd06\x9f\xc0\x8c '
>>> obj2.decrypt(cipher_text)
'abcdefghijklmnop'
