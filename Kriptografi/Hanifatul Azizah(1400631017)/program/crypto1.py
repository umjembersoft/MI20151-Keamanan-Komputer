from Crypto.Chiper import DES
des = DES.new('1234567', DES.MODE_ECB)
text = 'abcdefg'
ciper_text = des.encrypt(text)
ciper_text
'\xec\xc2\x9e\xd9] a\xd0'
des.decrypt(cipher_text)
'abcdefgh'
