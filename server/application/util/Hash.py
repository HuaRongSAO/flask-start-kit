from Crypto.Hash import SHA


def hash_encrypt(text):
    h = SHA.new()
    h.update(bytes(text, 'utf-8'))
    return h.hexdigest()
