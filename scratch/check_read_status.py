import re

with open("scratch/msg_list.html", "r", encoding="utf-8") as f:
    html = f.read()

tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
trs = tr_pattern.findall(html)

statuses = {}
for tr in trs:
    if "show-Message" in tr:
        # 获取第一个 td 的完整 HTML
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
        if tds:
            td0 = tds[0].strip()
            statuses[td0] = statuses.get(td0, 0) + 1

print("第一个 td 的内容统计:")
for td, cnt in statuses.items():
    print(f"Count: {cnt}")
    print(repr(td))
    print("-" * 20)
