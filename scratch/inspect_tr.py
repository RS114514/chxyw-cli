import re

with open("scratch/msg_list.html", "r", encoding="utf-8") as f:
    html = f.read()

tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
trs = tr_pattern.findall(html)

for tr in trs:
    if "物理作业：圆周运动" in tr:
        print("HTML for matching tr:")
        print(tr)
        break
