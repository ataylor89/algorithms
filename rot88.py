import argparse

def rot88(message):
    result = ''
    for character in message:
        code = ord(character)
        code = (code + 0x88000) % 0x110000
        result += chr(code)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='rot88.py', description='Encrypt or decrypt a message using rot88')
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
    output = rot88(message)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(output)
    else:
        print(output, end='')
