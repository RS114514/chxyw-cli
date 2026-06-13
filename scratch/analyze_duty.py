import re

with open("scratch/duty.html", "r", encoding="utf-8") as f:
    html = f.read()

# 找出所有的 tr 
tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
trs = tr_pattern.findall(html)

print(f"共有 {len(trs)} 个 tr。")

count = 0
for idx, tr in enumerate(trs):
    tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
    # 如果没有 td，看看有没有 th
    if not tds:
        tds = re.findall(r'<th[^>]*>(.*?)</th>', tr, re.DOTALL)
    if tds:
        count += 1
        clean_tds = []
        for td in tds:
            c = re.sub(r'<[^>]+>', '', td).strip()
            c = re.sub(r'\s+', ' ', c)
            clean_tds.append(c)
        print(f"Row {count}: {clean_tds}")
        if count >= 25:
            break
