import argparse

table = {}

for i in range(0, 26):
    table[chr(ord('a') + i)] = chr(ord('a') + (i + 13) % 26)
    table[chr(ord('A') + i)] = chr(ord('A') + (i + 13) % 26)

def rot13(message):
    result = ''
    for letter in message:
        substitution = table[letter] if letter in table else letter
        result += substitution
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='rot13.py', description='Encrypt or decrypt a message using rot13')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            message = file.read()
    else:
        message = args.message
    output = rot13(message)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(output)
    else:
        print(output, end='')
