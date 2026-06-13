import re

with open("scratch/hygiene_list.html", "r", encoding="utf-8") as f:
    html = f.read()

# 找出所有的 tr，看看它们的 td 元素
tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
trs = tr_pattern.findall(html)

print(f"共有 {len(trs)} 个 tr。")

count = 0
for idx, tr in enumerate(trs):
    tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
    if tds:
        count += 1
        clean_tds = []
        for td in tds:
            c = re.sub(r'<[^>]+>', '', td).strip()
            c = re.sub(r'\s+', ' ', c)
            clean_tds.append(c)
        print(f"Row {count}: {clean_tds}")
        # 看看 tr 里面是否有链接或者 ID 之类的
        links = re.findall(r'href=["\'](.*?)["\']', tr)
        print(f"  Links in row: {links}")
        if count >= 15:
            break
