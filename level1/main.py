#!/usr/bin/env python

CIPHERTEXT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# cipher looks as if it maps char x to char x + 2 (presumably, modulo 26)
MAP = {
    "k": "m",
    "o": "q",
    "e": "g",
}

URL = "http://www.pythonchallenge.com/pc/def/map.html"

def decrypt_char(c):
    """
    If c is a lowercase letter, move it two chars to the right.  Else return it unchanged.
    """
    first_letter = ord("a")
    last_letter  = ord("z")

    if ord(c) < first_letter or ord(c) > last_letter:
        return c

    # Calculate n - where c is the nth letter of the alphabet.  Add two and wrap round at 26.
    n = ord(c) - first_letter
    n = (n+2) % 26

    return chr(n + first_letter)

def decrypt(s):
    return "".join([decrypt_char(c) for c in s])

def main():
    print(decrypt(CIPHERTEXT))
    print(URL.replace("map", decrypt("map")))

if __name__ == '__main__':
    main()