import OS
From Crypto.Hash import MDS
def get_file_checksum(filename) :
h = MDS.new ()
chunk_sisse = 8192
with open (filename, 'rb') as f :
while True:
chunk = f.read(chunk_sisse)
if len(chunk) == 0:
break
h.update(chunk)
return h.hexdigest()