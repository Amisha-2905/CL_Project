from wxuniwx import wxtohin

def separate_tokens(sentence):
    # List of symbols to be separated
    symbols = [' ', ',', '।','?','|']
    symboll = ['-']

    # Replace symbols with space to split later
    for symbol in symbols:
        sentence = sentence.replace(symbol, ' ' + symbol)
    for symbol in symboll:
        sentence = sentence.replace(symbol, ' ' + symbol + ' ')
    
    # Split the sentence into tokens
    tokens = sentence.split()
    # print(tokens)
    out=[]
    for token in tokens:
        if token not in symbols and token not in symboll:
            word = wxtohin(token)
            out.append(word)
            continue
        out.append(token)
    return out

def write_tokens_to_file(tokens, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for token in tokens:
            file.write(token + '\n')

def wxmain():
    # Input Hindi sentence
    wx_sentence = input("Enter the WX sentence: ")

    # Separate tokens
    tokens = separate_tokens(wx_sentence)
    
    # Write tokens to file
    output_file = "tokens.txt"
    write_tokens_to_file(tokens, output_file)
    print(f"Tokens are written to {output_file}")


if __name__ == "__main__":
    wxmain()
# sentence = input()
# print(separate_tokens(sentence))