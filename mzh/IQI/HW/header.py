#!/usr/bin/env/python3

import sys, os
head = open("header.txt", encoding='utf-8')
header = head.read()
head.close()

if len(sys.argv) == 1
    print("Usage: ./header.py filename.md")
else
    path = sys.argv[1]
    if os.path.exists(path):
        file = open(path, encoding='utf-8')
        s = header + file.read()
        file.close()
        file = open(path, 'w', encoding='utf-8')
        file.write(s)
        file.close()
    else
        file = open(path, 'w', encoding='utf-8')
        file.write(header)
        file.close()