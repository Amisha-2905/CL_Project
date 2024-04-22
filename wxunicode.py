import re
import sys
import random
import string
import subprocess
import pandas as pd

# hin_vowels = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ"]
# hin_sonorants = ["ऋ", "ॠ", "ऌ"]
# hin_anuswara = ["अं"]
# hin_nukta = ["़"]
# hin_consonants = [
#     "क", "ख", "ग", "घ", "ङ",
#     "च", "छ", "ज", "झ", "ञ",
#     "ट", "ठ", "ड", "ढ", "ण",
#     "त", "थ", "द", "ध", "न",
#     "प", "फ", "ब", "भ", "म",
#     "य", "र", "ल", "व",
#     "श", "ष", "स", "ह"
# ]

hin2wx_vowels = {
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
    "ै": "E",
    "ा": "A",
    "ो": "o",
    "ू": "U",
    "ु": "u",
    "ि": "i",
    "ी": "I",
    "े": "e",
    "ऑ": "OY",
    "ॅ": "EY",
}
hin2wx_sonorants = {
    "ऋ": "q",
    "ॠ": "Q",
    "ऌ": "L"
}
hin2wx_anuswara = {"अं": "M", "ं": "M", "ँ": "z", "अँ": "z"}
hin2wx_consonants = {
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

hin2wx_all = {
    **hin2wx_vowels, **hin2wx_anuswara,
    **hin2wx_sonorants, **hin2wx_consonants
}

def is_vowel_hin(char):
    """
    Checks if the character is a vowel.
    """
    if char in hin2wx_anuswara or char in hin2wx_vowels:
        return True
    return False


def hin2wx(hin_string):
    """
    Converts the Hindi string to the WX string.

    This function goes through each character from the hin_string and
    maps it to a corresponding Roman character according to the
    Devanagari to Roman character mapping defined previously.
    """
    wx_string = []
    for i, current_char in enumerate(hin_string[:-1]):
        # skipping over the character as it's not included
        # in the mapping
        if current_char == "्":
            continue

        # get the Roman character for the Devanagari character
        wx_string.append(hin2wx_all[current_char])

        # Handling of "a" sound after a consonant if the next
        # character is not "्" which makes the previous character half
        if not is_vowel_hin(current_char):
            if hin_string[i+1] != "्" and not is_vowel_hin(hin_string[i+1]):
                wx_string.append(hin2wx_all["अ"])

    wx_string.append(hin2wx_all[hin_string[-1]])
    if not is_vowel_hin(hin_string[-1]):
        wx_string.append(hin2wx_all["अ"])

    wx_string = "".join(wx_string)

    # consonant + anuswara should be replaced by
    # consonant + "a" sound + anuswara
    reg1 = re.compile("([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])M")
    wx_string = reg1.sub("\g<1>aM", wx_string)

    # consonant + anuswara should be replaced by
    # consonant + "a" sound + anuswara
    reg1 = re.compile("([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSRsh])M")
    wx_string = reg1.sub("\g<1>aM", wx_string)

    return wx_string

# hindi = input()
# wx = hin2wx(hindi)
# print(wx)

# a ke cases, dictionary add, multi line input with space

# Your existing code for Hindi to WX conversion goes here...

def get_inflections(wx_string):
    """
    Uses LT Toolbox to get inflections of a given word in WX notation.
    """
    # Assuming lt-comp is the LT Toolbox command-line tool for compiling dictionaries
    lt_comp_command = ["lt-comp", "lr", "para.dix", "out.bin"]

    # Run lt-comp to compile the dictionary
    subprocess.run(lt_comp_command)

    # Assuming lt-proc is the LT Toolbox command-line tool for processing compiled dictionaries
    lt_proc_command = ["lt-proc", "-c", "out.bin"]

    # Use subprocess to run the command and capture the output
    lt_proc_output = subprocess.run(lt_proc_command, input=wx_string, text=True, capture_output=True)

    # Decode the output and return it
    return lt_proc_output.stdout

# Get input in Hindi Unicode
hindi_unicode_input = input()

# Convert Hindi Unicode to WX notation
wx_output = hin2wx(hindi_unicode_input)

# Get inflections using LT Toolbox
inflections_output = get_inflections(wx_output)

# Print the inflections
# print("Inflections:")
print(inflections_output)
