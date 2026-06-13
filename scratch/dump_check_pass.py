with open("scratch/file_interface.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
s = scripts[14]

lines = s.split('\n')
# 找到 check_Password() 所在的行，并打印其后 60 行
for j, line in enumerate(lines):
    if "function check_Password" in line:
        print('\n'.join(lines[j:j+60]))
        break
