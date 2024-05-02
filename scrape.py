import re

def extract_words_tags_from_sentence(sentence):
    pattern = r'\d+\.\d+\s+(\S+)\s+(\S+)'
    matches = re.findall(pattern, sentence)
    words_tags = [(match[0], match[1]) for match in matches]
    return words_tags

with open('output.txt', 'w') as output_file:
    for i in range(1,3001, 50):
        start_range = i
        end_range = i + 49
        filename = f"CL-Project Dataset/Training Data/mor-{start_range}-{end_range}-posn-name.txt"
        with open(filename, 'r') as input_file:
            data = input_file.read().rstrip()
            sentences = data.strip().split('\n\n')
            for sentence in sentences:
                words_tags = extract_words_tags_from_sentence(sentence)
                for word, tag in words_tags:
                    output_file.write(f"{word}\t{tag}\n")
                if sentence != sentences[-1]:
                    output_file.write('\n')

with open('output.txt', 'r+') as file:
    content = file.read()
    content = content.replace('\n\n\n','\n\n')
    file.seek(0)
    file.write(content)