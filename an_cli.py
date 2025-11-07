#!/usr/bin/env python3
"""Small CLI compatible with node js_helper.js for quick integration tests.

Usage:
    python an_cli.py gen
    python an_cli.py sign <hash> <key>
    python an_cli.py open <message>
"""
import sys
from anproto.an import Gen, Sign, Open, Hash


def main(argv):
    if len(argv) < 2:
        print("missing cmd")
        return 2
    cmd = argv[1]
    if cmd == "gen":
        print(Gen())
        return 0
    if cmd == "sign":
        if len(argv) < 4:
            print("usage: sign <hash> <key>")
            return 2
        h = argv[2]
        k = argv[3]
        print(Sign(h, k))
        return 0
    if cmd == "open":
        if len(argv) < 3:
            print("usage: open <message>")
            return 2
        m = argv[2]
        print(Open(m))
        return 0
    print("unknown cmd")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
