import re

with open("scratch/msg_list.html", "r", encoding="utf-8") as f:
    html = f.read()

tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
trs = tr_pattern.findall(html)

for i, tr in enumerate(trs[:10]):
    if "show-Message" in tr:
        # 打印这个 tr 里面，除了删除和转发外的所有 HTML 块，看看是否有 class 或者 strong 标签
        print(f"--- TR {i} ---")
        # 查找 title 所在的 td
        tds = re.findall(r'<td>(.*?)</td>', tr, re.DOTALL)
        for td in tds:
            if "show-Message" in td:
                print(repr(td.strip()))
