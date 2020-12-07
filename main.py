from argparse import ArgumentParser

from certifire import Certifire

def argparse():
    parser = ArgumentParser(description="CertiFire scripts for Certifire")
    subparsers = parser.add_subparsers()

    get_p = subparsers.add_parser('get')
    get_p.add_argument("key", metavar='key', help='Certificate ID or Search string')

    new_p = subparsers.add_parser("new")
    new_p.add_argument("name", metavar='n', help='Certificate name (fqdn)')
    new_p.add_argument('-o', help='Owner of certificate', dest='owner')
    new_p.add_argument('-a', help='Issuing Authority', dest='auth')

    return parser.parse_args()


if __name__ == "__main__":
    args = argparse()
    L = Certifire()

    if 'key' in args:
        print(L.getCertificates(args.key))
    else:
        print(L.newCert(args.name, args.owner, args.auth))
