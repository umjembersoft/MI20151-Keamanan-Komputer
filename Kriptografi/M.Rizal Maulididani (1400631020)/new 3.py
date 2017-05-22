>>> des = DES.new('01234567', DES.MODE_ECB)
>>> text = 'abcdefgh'
>>> cipher_text = des.encrypt(text)
>>> cipher_text
'\xec\xc2\x9e\xd9] a\xd0'
>>> des.decrypt(cipher_text)
'abcdefgh'