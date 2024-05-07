import re

def verbmain():
    with open("output.txt", 'r', encoding='utf-8') as input_file:
        text = input_file.read()

        pattern1 = r'(\S+)\t+(V_VM|V_VAUX)\n'

        matches1 = re.findall(pattern1, text)

        verbs = [match[0] for match in matches1 if match[1].startswith('V_VM') or match[1].startswith('V_VAUX')]

        for verb in verbs:
            print(f"Verb: {verb}")

        with open('verbs_output.txt', 'w', encoding='utf-8') as output_file:
            for verb in verbs:
                output_file.write(f"{verb}\n")

if __name__ == "__main__":
    verbmain()