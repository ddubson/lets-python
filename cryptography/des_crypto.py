# DES - Data Encryption Standard (Symmetric Key)
from Crypto.Cipher import DES
from Crypto import Random

# Initialization Vector (8 bytes)
init_vector = Random.new().read(DES.block_size)

# Output Feedback Mode (1 of 5 available)
mode = DES.MODE_OFB


def des_encrypt(key, plaintext):
    cipher = DES.new(key, mode, init_vector)
    return cipher.encrypt(plaintext)


def des_decrypt(key, ciphertext):
    cipher = DES.new(key, mode, init_vector)
    return cipher.decrypt(ciphertext)


def main():
    key = b'8byt key'  # 64-bit key (8 bytes)
    plaintext = "sona si latine loqueris "

    ciphertext = des_encrypt(key, plaintext)
    print "plaintext: {0}\nciphertext (hex): {1}".format(plaintext, ciphertext.encode('hex'))

    decrypted = des_decrypt(key, ciphertext)
    print "decrypted plaintext: {0}".format(decrypted)


if __name__ == '__main__':
    main()
