import os
from Crypto.Cipher import DES3

def encrypt_file(in_filename,out_filename,  chunk_size, key,iv):
des3 = DES3.new (key, DES3.MODE_CFB, iv)
chunk = if_file.read(chunk_size)
if len (chunk) % 16 != 0;
	break
	elif len (chunk) % 16 != 0;
		chunk += ''* (16 - len (chunk) % 16)
	out_file.write(des3.encrypt(chunk))
def decrypth_file (in_filename, out_filename, chunk_size, key, iv):
	des3 = DES3.new(key, DES3.MODE_CFB, iv)
	with open(in_filename, 'r') as in_file:
	with open(out_filename, 'w') as out_file:
	while True:
	chunk = in_file.read(chunk_size
	if len(chunk) == 0:
	break
	out_file.write(des3.decrypt (chunk))