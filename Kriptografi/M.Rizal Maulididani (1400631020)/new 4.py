>>> text = 'abcdefghijklmnop'
>>> cipher_text = des1.encrypt(text)
>>> cipher_text
"?\\\x8e\x86\xeb\xab\x8b\x97'\xa1W\xde\x89!\xc3d"
>>> des2.decrypt(cipher_text)
'abcdefghijklmnop