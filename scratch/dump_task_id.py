with open("scratch/file_interface.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
s = scripts[14]

lines = s.split('\n')
for j, line in enumerate(lines):
    if "task_id" in line:
        # 打印这一行前后的 5 行
        start = max(0, j - 2)
        end = min(len(lines), j + 6)
        print(f"Match around line {j+1}:")
        print('\n'.join(lines[start:end]))
        print("-" * 20)
