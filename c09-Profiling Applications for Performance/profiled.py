import cProfile
import hashlib


def encrypt_password(password, salt):
    """
    Encrypt the provided password.
    Keyword arguments:
        password – The password to be encrypted
        salt – The salt to be used for padding the password
    Returns:
        String
    """
    profiler = cProfile.Profile()
    profiler.enable()
    passwd_hash = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=password.encode('utf-8'),
        salt=salt,
        iterations=10000,
        dklen=None
    )
    passwd_hash_hex = passwd_hash.hex()
    profiler.disable()
    profiler.print_stats()
    return passwd_hash_hex
