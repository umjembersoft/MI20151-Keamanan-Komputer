text = 'abcdefgh'
hash = SHA256.new(text).digest()
public_key.verify(hash, signature)
True