import argparse

x = 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default='track2_90.dat',action='store', help='scan pattern file name.')
    parser.add_argument('-m', action='store_true', help='Mointering scan pattern')
    args = parser.parse_args()
    print(args.f)
    print(args.m)

    if args.m:
        print('Mointering scan pattern.')