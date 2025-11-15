import argparse

def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    msgcodes = list(map(lambda x: ord(x), msg))
    keycodes = list(map(lambda x: ord(x), key))
    out = [chr(msgcodes[i] ^ keycodes[i % keylen]) for i in range(0, msglen)]
    return ''.join(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='xor.py', description='Encrypt or decrypt a message')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-k', '--keyfile', type=str, default='key.txt')
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            msg = file.read()
    else:
        msg = args.message
    with open(args.keyfile, 'r') as file:
        key = file.read()
    output = crypt(msg, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(output)
    else:
        print(output, end='')
