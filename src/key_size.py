from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
private_key = dsa.generate_private_key(
    key_size=512,
    backend=default_backend()
)

from Crypto.Hash import SHA256
val = SHA256.new('abc'.encode('utf-8')).hexdigest()