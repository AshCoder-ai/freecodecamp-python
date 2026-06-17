"""
Caesar Cipher Module

This module implements a basic Caesar cipher for encrypting and decrypting
text by shifting letters in the alphabet. It supports both uppercase and
lowercase translation.
"""


def caesar(text, shift, encrypt=True):
    """
    Encrypts or decrypts the input text using a Caesar cipher translation.

    Args:
        text (str): The string to be encrypted or decrypted.
        shift (int): The alphabet shift value (must be between 1 and 25).
        encrypt (bool, optional): If True, encrypts the text; if False, decrypts it. Defaults to True.

    Returns:
        str: The encrypted or decrypted text, or an error message if the shift is invalid.
    """
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    """
    Encrypts the input text by calling caesar with the specified shift.

    Args:
        text (str): The string to be encrypted.
        shift (int): The alphabet shift value (must be between 1 and 25).

    Returns:
        str: The encrypted text.
    """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Decrypts the input text by calling caesar with the specified shift in reverse.

    Args:
        text (str): The string to be decrypted.
        shift (int): The alphabet shift value (must be between 1 and 25).

    Returns:
        str: The decrypted text.
    """
    return caesar(text, shift, encrypt=False)


encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)