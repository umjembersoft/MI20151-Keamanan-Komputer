>>> from Crypto.Cipher import DES
>>> from Crypto import Random
>>> iv = Random.get_random_bytes(8)
>>> des1 = DES.new('01234567', DES.MODE_CFB, iv)
>>> des2 = DES.new('01234567', DES.MODE_CFB, iv)
>>> text = 'abcdefghijklmnop'
>>> cipher_text = des1.encrypt(text)
>>> cipher_text
"?\\\x8e\x86\xeb\xab\x8b\x97'\xa1W\xde\x89!\xc3d"
>>> des2.decrypt(cipher_text)
'abcdefghijklmnop'
