from Crypto.Hash import SHA256
def check_password(clear_password, password_hash):
return SHA256. new(clear_password) . hexdi gest() == password_hash