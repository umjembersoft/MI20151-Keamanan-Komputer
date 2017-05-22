from Crypto import Random
02 iv = Random.get_random_bytes(8)
03 with open('to_enc.txt', 'r') as f:
04 print 'to_enc.txt: %s' % f.read()
05 encrypt_file('to_enc.txt', 'to_enc.enc', 8192, key, iv)
06 with open('to_enc.enc', 'r') as f:
07 print 'to_enc.enc: %s' % f.read()
08 decrypt_file('to_enc.enc', 'to_enc.dec', 8192, key, iv)
09 with open('to_enc.dec', 'r') as f:
10 print 'to_enc.dec: %s' % f.read()