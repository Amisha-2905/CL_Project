import re
import sys
import random
import string
import subprocess
import pandas as pd

hintowx_vowels_matra = {
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

hintowx_vowels_full = {
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

hintowx_sonorants = {
    "ऋ": "q",
    "ॠ": "Q",
    "ऌ": "L"
}

hintowx_anuswara = {"ं": "M", "ँ": "z", "ः": "H"}

hintowx_consonants = {
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

hintowx_all = {
    **hintowx_vowels_matra, **hintowx_vowels_full, **hintowx_anuswara,
    **hintowx_sonorants, **hintowx_consonants
}

wxtohin_all = {
    **wxtohin_vowels_matra,
    **wxtohin_vowels_half,
    **wxtohin_sonorants,
    **wxtohin_anuswara,
    **wxtohin_anuswara_half,
    **wxtohin_consonants
}

def is_vowel_matra(char):
    if char in hintowx_vowels_matra:
        return True
    return False

def is_vowel_full(char):
    if char in hintowx_vowels_full:
        return True
    return False

def is_vowel_anuswara(char):
    if char in hintowx_anuswara:
        return True
    return False

def is_sonorants(char):
    if char in hintowx_sonorants:
        return True
    return False

def is_consonant(char):
    if char in hintowx_consonants:
        return True
    return False

def is_vowel(char):
    if char in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "M", "z", "H"}:
        return True
    return False

def hintowx(hin_string):
    wx_string = []

    for i, current_char in enumerate(hin_string[:-1]):
        if current_char == "्":
            continue
        wx_string.append(hintowx_all[current_char])
        if not is_vowel_full(current_char) and is_consonant(hin_string[i]) and not is_vowel_matra(hin_string[i+1]) and hin_string[i+1] != "्":
            wx_string.append(hintowx_all["अ"])

    wx_string.append(hintowx_all[hin_string[-1]])

    if not is_sonorants(hin_string[-1]) and not is_vowel_anuswara(hin_string[-1]) and not is_vowel_full(hin_string[-1]) and not is_vowel_matra(hin_string[-1]):
        wx_string.append(hintowx_all["अ"])

    wx_string = "".join(wx_string)
    return wx_string

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

def get_inflections(wx_string):
    lt_proc_command = ["lt-proc", "-c", "out.bin"]

    lt_proc_output = subprocess.run(lt_proc_command, input=wx_string, text=True, capture_output=True)

    return lt_proc_output.stdout

def func(string):
    str = string.split('/')
    inflections = str[0].split('^')
    inflection = wxtohin(inflections[1])
    out=[]
    out.append('^')
    out.append(inflection)
    for i in range(1,len(str)):
        out.append('/')
        inflections=str[i].split('<')
        out.append(wxtohin(inflections[0]))
        for j in range(1,len(inflections)):
            out.append('<'+inflections[j])
    return "".join(out)

lt_comp_command = ["lt-comp", "lr", "dictionary.dix", "out.bin"]
subprocess.run(lt_comp_command)

word=input()
# print(get_inflections(hintowx(word)))
print(func(get_inflections(hintowx(word))))
# print(hintowx(word))
# print(wxtohin(hintowx(word)))
# with open('abc.txt', 'w') as file:
#     file.write(get_inflections(hintowx(word)))
