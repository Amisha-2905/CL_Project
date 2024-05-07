def separate_tokens(sentence):
    # List of symbols to be separated
    symbols = [' ', ',', '।','?']
    symboll = ['-']

    # Replace symbols with space to split later
    for symbol in symbols:
        sentence = sentence.replace(symbol, ' ' + symbol)
    for symbol in symboll:
        sentence = sentence.replace(symbol, ' ' + symbol + ' ')
    
    # Split the sentence into tokens
    tokens = sentence.split()

    return tokens

def write_tokens_to_file(tokens, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for token in tokens:
            file.write(token + '\n')

def hindimain():
    # Input Hindi sentence
    hindi_sentence = input("Enter the Hindi sentence: ")

    # Separate tokens
    tokens = separate_tokens(hindi_sentence)

    # Write tokens to file
    output_file = "tokens.txt"
    write_tokens_to_file(tokens, output_file)
    print(f"Tokens are written to {output_file}")

if __name__ == "__main__":
    hindimain()
