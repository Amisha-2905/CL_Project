import re
import sys
import random
import string
import subprocess
import pandas as pd
vowels_matra = {
    "ै": "E",
    "ा": "A",
    "ो": "o",
    "ू": "U",
    "ु": "u",
    "ि": "i",
    "ी": "I",
    "े": "e",
    "ॅ": "EY",
    "ृ": "q",
}
vowels_full = {
    "अ": "a",
    "आ": "A",
    "इ": "i",
    "ई": "I",
    "उ": "u",
    "ऊ": "U",
    "ए": "e",
    "ऐ": "E",
    "ओ": "o",
    "औ": "O",
    "ऑ": "OY",
}
sonorants = {
    "ऋ": "q",
    "ॠ": "Q",
    "ऌ": "L"
}
anuswara = {"ं": "M", "ँ": "z", "ः": "H"}
consonants = {
    "क": "k",
    "ख": "K",
    "ग": "g",
    "घ": "G",
    "ङ": "f",
    "च": "c",
    "छ": "C",
    "ज": "j",
    "झ": "J",
    "ञ": "F",
    "ट": "t",
    "ठ": "T",
    "ड": "d",
    "ढ": "D",
    "ण": "N",
    "त": "w",
    "थ": "W",
    "द": "x",
    "ध": "X",
    "न": "n",
    "प": "p",
    "फ": "P",
    "ब": "b",
    "भ": "B",
    "म": "m",
    "य": "y",
    "र": "r",
    "ल": "l",
    "व": "v",
    "श": "S",
    "ष": "R",
    "स": "s",
    "ह": "h",
}
all = {
    **vowels_matra, **vowels_full, **anuswara,
    **sonorants, **consonants
}
def is_vowel_matra(char):
    if char in vowels_matra:
        return True
    return False
def is_vowel_full(char):
    if char in vowels_full:
        return True
    return False
def is_vowel_anuswara(char):
    if char in anuswara:
        return True
    return False
def is_sonorants(char):
    if char in sonorants:
        return True
    return False
def is_consonant(char):
    if char in consonants:
        return True
    return False
def hin2wx(hin_string):
    wx_string = []
    for i, current_char in enumerate(hin_string[:-1]):
        if current_char == "्":
            continue
        wx_string.append(all[current_char])
        if not is_vowel_full(current_char) and is_consonant(hin_string[i]) and not is_vowel_matra(hin_string[i+1]) and hin_string[i+1] != "्":
            wx_string.append(all["अ"])
    wx_string.append(all[hin_string[-1]])
    if not is_sonorants(hin_string[-1]) and not is_vowel_anuswara(hin_string[-1]) and not is_vowel_full(hin_string[-1]) and not is_vowel_matra(hin_string[-1]):
        wx_string.append(all["अ"])
    wx_string = "".join(wx_string)
    return wx_string
hindi = input()
wx = hin2wx(hindi)
print(wx)
