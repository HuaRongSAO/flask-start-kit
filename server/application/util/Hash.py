from Crypto.Hash import SHA


def hash_encrypt(text):
    h = SHA.new()
    h.update(text)
    return h.hexdigest()
