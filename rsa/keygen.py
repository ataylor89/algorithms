import primetable
import keytable
import random
import argparse

def create_key_pair(keylen, tmin, tmax):
    keytable.load()
    filtered = {}
    for k,v in keytable.table.items():
        if v[1] >= tmin and v[1] <= tmax and v[2] >= tmin and v[2] <= tmax:
            filtered[k] = v
    if keylen > len(filtered):
        raise ValueError('There aren\'t enough keys in the key table that meet the criteria')
    nvalues = list(filtered.keys())
    nvalues = random.sample(nvalues, keylen)
    key = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = filtered[nvalue]
        key.append((n, e, d))
    return key

def main():
    primetable.load()
    parser = argparse.ArgumentParser(prog='keygen.py', description='Create a public key and a private key')
    parser.add_argument('-kl', '--keylength', type=int, required=True)
    parser.add_argument('-tmin', '--min_threshold', type=float, default=0)
    parser.add_argument('-tmax', '--max_threshold', type=float, default=primetable.get(-1))
    parser.add_argument('-o', '--outputfile', type=str, default='key.txt')
    args = parser.parse_args()
    keylen = args.keylength
    tmin = int(args.min_threshold)
    tmax = int(args.max_threshold)
    try:
        key = create_key_pair(keylen, tmin, tmax)
    except Exception as err:
        print(err)
        return
    with open(args.outputfile, 'w') as file:
        for (n, e, d) in key:
            file.write("n=%d e=%d d=%d\n" %(n, e, d))
        print('Created keyfile %s' %args.outputfile)
    
if __name__ == '__main__':
    main()
