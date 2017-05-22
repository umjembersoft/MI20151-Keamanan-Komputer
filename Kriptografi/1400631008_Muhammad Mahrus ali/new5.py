>>> from Crypto.Ciper import DES
>>> from Crypto import Random
>>> iv = Random.get_random_bytes(8)
>>> text = 'abcdefghijklmnop'
>>> des1 = DES.new ('1234567', DES.MODE_CFB, iv)
>>> des2 =DES.new ('1234567', DES.MODE_CFB, iv)
>>> text = 'abcdefghijklmnop'
>>> ciper_text = des1.encrypt(ciper_text)
"?\\\x8e\xb6\xeb\xab\x8b\x97'\xawlW\xde\x89!\xc3d"
>>> des2.decrypt(ciper_text)
'abcdefghijklmnop'
