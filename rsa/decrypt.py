import os
import parser
import util
import argparse

def decrypt(ciphertext, key):
    message = ''
    keylen = len(key)
    start = 0
    end = 0
    i = 0
    while start < len(ciphertext):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        end = start + size
        substr = ciphertext[start:end]
        cipher = util.decode(substr)
        message += chr(util.power_mod_n(cipher, d, n))
        i += 1
        start += size
    return message

def main():
    home_dir = os.path.expanduser('~')
    default_key = f'{home_dir}/Github/rsa/keys/default.txt'
    argparser = argparse.ArgumentParser(prog='decrypt.py', description='Decrypt a message')
    argparser.add_argument('-i', '--inputfile', type=str, required=True)
    argparser.add_argument('-k', '--keyfile', type=str, default=default_key)
    argparser.add_argument('-o', '--outputfile', type=str)
    args = argparser.parse_args()
    with open(args.inputfile, 'rb') as file:
        ciphertext = file.read()
    ciphertext = ciphertext.decode('utf-8')
    key = parser.parse_key(args.keyfile)
    msg = decrypt(ciphertext, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(msg)
    else:
        print(msg, end='')

if __name__ == '__main__':
    main()
