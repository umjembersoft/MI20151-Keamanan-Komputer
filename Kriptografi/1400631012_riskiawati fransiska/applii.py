from Crypto import Random
iv = Random.get_random_bytes(8)
with open('to_enc.txt', 'r') as f:
print 'to_enc.txt: %s' % f.read()
encrypt_file('to_enc.txt', 'to_enc.enc', 8192, key, iv)
with open('to_enc.enc', 'r') as f:
print 'to_enc.enc: %s' % f.read()
decrypt_file('to_enc.enc', 'to_enc.dec', 8192, key, iv)
with open('to_enc.dec', 'r') as f:
print 'to_enc.dec: %s' % f.read()