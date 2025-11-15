import os
import parser
import util
import argparse

def encrypt(msg, key):
    ciphertext = ''
    codes = msg.encode('utf-8')
    keylen = len(key)
    for i in range(0, len(codes)):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        cipher = util.power_mod_n(codes[i], e, n)
        encoding = util.encode(cipher, size)
        ciphertext += encoding
    return ciphertext

def main():
    home_dir = os.path.expanduser('~')
    default_key = f'{home_dir}/Github/rsa/keys/default.txt'
    argparser = argparse.ArgumentParser(prog='encrypt.py', description='Encrypt a message')
    group = argparser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    argparser.add_argument('-k', '--keyfile', type=str, default=default_key)
    argparser.add_argument('-o', '--outputfile', type=str)
    args = argparser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            msg = file.read()
    else:
        msg = args.message
    key = parser.parse_key(args.keyfile)
    ciphertext = encrypt(msg, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(ciphertext)
    else:
        print(ciphertext, end='')

if __name__ == '__main__':
    main()
