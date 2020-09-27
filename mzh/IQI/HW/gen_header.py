#!/usr/bin/env python3

import sys, os, re
header_file = open('header.txt', encoding='utf-8')
header = header_file.read()
header_file.close()

if len(sys.argv) == 1:
    print("[Usage]\n\t./gen_header.py filename.md")
else:
    path = sys.argv[1]
    if os.path.exists(path):
        file = open(path, encoding='utf-8')
        s = file.read()

        match = re.match(r'\$\$(?:\$(?!\$)|[^\$])*\$\$', s) # match从头匹配, search可以不从头匹配, 均匹配一次即返回
        if match:
            s = s.replace(match.group(), header, 1) # 替换一次
        else:
            s = header + s

        file.close()
        file = open(path, 'w', encoding='utf-8')
        file.write(s)
        file.close()
    else:
        file = open(path, 'w', encoding='utf-8')
        file.write(header)
        file.close()