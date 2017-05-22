>>> from Crypto.Ciper import DES
>>> des = DES.new ('01234567', DES.MODE_ECB)
>>> ciper_text = des.encrypt(text)
>>> ciper_text
'\xec\xc2\x9e\xd9] a\xd0'
>>> des.decrypt (ciper_text)
'abcdefgh'