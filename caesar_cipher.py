# Encrypt

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(message, skip):
    """takes in string and returnes encrypted one

    Args:
        message (str): string to be encrypted
        skip (int): the cypher key
    """

    encrypted_message = ""
    for letter in message.lower():

        shift = (alphabet.index(letter) + skip) % len(alphabet)
        encrypted_message += alphabet[shift]
    return encrypted_message


def decrypt(message, cypher_key):

    decrypted_message = ""

    for letter in message.lower():
        shift = (alphabet.index(letter) - cypher_key) % len(alphabet)
        decrypted_message += alphabet[shift]
    return decrypted_message


message = "cocumickkte"
cypher_key = 3
encrypted_message = encrypt(message, cypher_key)
print(encrypted_message)
decrypted_message = decrypt(encrypted_message, cypher_key)
print(decrypted_message)
