import re
import sys
import random
import string
import subprocess
import pandas as pd

wxtohin_vowels_matra = {
    "a": "अ",
    "A": "आ",
    "i": "इ",
    "I": "ई",
    "u": "उ",
    "U": "ऊ",
    "e": "ए",
    "E": "ऐ",
    "o": "ओ",
    "O": "औ",
    "z": "ँ",
    "H": "ः"
}
wxtohin_vowels_half = {
    "A": "ा",
    "e": "े",
    "E": "ै",
    "i": "ि",
    "I": "ी",
    "o": "ो",
    "U": "ू",
    "u": "ु",
    "z": "ँ",
    "H": "ः",
    "EY":"ॅ",
    "q":"ृ"
}
wxtohin_sonorants = {
    "q": "ऋ",
    "Q": "ॠ",
    "L": "ऌ"
}
wxtohin_anuswara = {"M": "अं"}
wxtohin_anuswara_half = {"M": "ं"}
wxtohin_consonants = {
    "k": "क",
    "K": "ख",
    "g": "ग",
    "G": "घ",
    "f": "ङ",
    "c": "च",
    "C": "छ",
    "j": "ज",
    "J": "झ",
    "F": "ञ",
    "t": "ट",
    "T": "ठ",
    "d": "ड",
    "D": "ढ",
    "N": "ण",
    "w": "त",
    "W": "थ",
    "x": "द",
    "X": "ध",
    "n": "न",
    "p": "प",
    "P": "फ",
    "b": "ब",
    "B": "भ",
    "m": "म",
    "y": "य",
    "r": "र",
    "l": "ल",
    "v": "व",
    "S": "श",
    "R": "ष",
    "s": "स",
    "h": "ह",
}
wxtohin_all = {
    **wxtohin_vowels_matra,
    **wxtohin_vowels_half,
    **wxtohin_sonorants,
    **wxtohin_anuswara,
    **wxtohin_anuswara_half,
    **wxtohin_consonants
}

def is_vowel(char):
    if char in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "M", "z", "H"}:
        return True
    return False


def wxtohin(wx_string):
    wx_string += " "
    hin_string = []
    for i, roman_char in enumerate(wx_string[:-1]):
        if is_vowel(roman_char):
            if roman_char == "a" and i != 0:
                continue

            if roman_char == "M":
                hin_string.append(wxtohin_anuswara_half[roman_char])
            elif i == 0 or wx_string[i-1] in wxtohin_vowels_half:
                hin_string.append(wxtohin_vowels_matra[roman_char])
            else:
                hin_string.append(wxtohin_vowels_half[roman_char])
        else:
            hin_string.append(wxtohin_all[roman_char])
            if not is_vowel(wx_string[i+1]) and wx_string[i+1] != " ":
                hin_string.append("्")
    return "".join(hin_string)

word = input()
uni = wxtohin(word)
print(uni)
