#!/usr/bin/env python3

# TODO keyboard-layout-agnostic

from sys import argv
import subprocess

HOME_ROW = 'AOEUIDHTNS'

def main():
    args = ['git'] + argv[1:]
    for i, arg in enumerate(args):
        if match(arg):
            args[i] = fix(arg)
            break
    subprocess.call(args)

def match(arg):
    hash_chars = set('abcdef0123456789')
    vertigo_chars = set(HOME_ROW)
    all_chars = hash_chars | vertigo_chars

    if any(char not in all_chars for char in arg):
        return False
    return True

def fix(commithash):
    if commithash == 'HEAD':
        print(' - HEAD (ignored)')
        return 'HEAD'
    result = commithash.translate(str.maketrans(HOME_ROW, '1234567890'))
    print(' -', commithash, '->', result)
    return result

if __name__ == '__main__':
    main()
