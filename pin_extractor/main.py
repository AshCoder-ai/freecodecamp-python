"""
Pin Extractor Module

This module provides functionality to extract secret PIN codes from poems.
Each PIN is constructed by taking the length of the N-th word of the N-th line
(0-indexed) in each poem. If a line is too short, '0' is used.
"""


def pin_extractor(poems):
    """
    Extracts a list of secret PIN codes from a collection of poems.

    For each poem, the code is formed by examining each line (index `i`).
    If the line contains more than `i` words, the length of the `i`-th word
    is appended to the code. Otherwise, '0' is appended.

    Args:
        poems (list of str): A list of poems, where each poem is a multiline string.

    Returns:
        list of str: The extracted secret PIN codes for each poem.
    """
    secret_codes = []
    for poem in poems:
        secret_code = ""
        lines = poem.split("\n")
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"
        secret_codes.append(secret_code)
    return secret_codes



poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
poem3 = "There\nonce\nwas\na\ndragon"

print(pin_extractor([poem, poem2, poem3]))
