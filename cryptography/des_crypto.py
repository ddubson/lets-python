from Crypto.Cipher import DES
from Crypto import Random

init_vector = Random.new().read(DES.block_size)
mode = DES.MODE_OFB


def des_encrypt(key, plaintext):
    cipher = DES.new(key, mode, init_vector)
    return cipher.encrypt(plaintext)


def des_decrypt(key, ciphertext):
    cipher = DES.new(key, mode, init_vector)
    return cipher.decrypt(ciphertext)


def main():
    key = b'8bit key'
    plaintext = "sona si latine loqueris "

    ciphertext = des_encrypt(key, plaintext)
    print "plaintext: {0}\nciphertext (hex): {1}".format(plaintext, ciphertext.encode('hex'))

    decrypted = des_decrypt(key, ciphertext)
    print "decrypted plaintext: {0}".format(decrypted)


if __name__ == '__main__':
    main()
