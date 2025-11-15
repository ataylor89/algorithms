import random
import argparse

def create_key(key_length):
    key = [chr(random.randint(0, 255)) for i in range(0, key_length)]
    return ''.join(key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='keygen.py', description='Create an XOR key')
    parser.add_argument('-kl', '--keylength', type=int, default=64)
    parser.add_argument('-o', '--outputfile', type=str, default='key.txt')
    args = parser.parse_args()
    key = create_key(args.keylength)
    with open(args.outputfile, 'w') as file:
        file.write(key)
