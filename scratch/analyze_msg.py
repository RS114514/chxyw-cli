import re

with open("scratch/msg_list.html", "r", encoding="utf-8") as f:
    html = f.read()

# 提取 show-Message 链接
matches = re.findall(r'href=["\']/sitemessage/show-Message/(\d+)/["\'].*?>(.*?)</a>', html)
print(f"找到 {len(matches)} 个包含 show-Message 的链接:")
for m in matches[:15]:
    # 清理可能存在的 span 标签
    title = re.sub(r'<[^>]+>', '', m[1]).strip()
    print(f"  ID: {m[0]}, Title: {title}")

# 提取 tr 中的各项
# 让我们找出包含 show-Message/(\d+)/ 的 <tr> 块
# 每个 tr 的结构通常是：
# <tr>
#   <td>序号</td>
#   <td><a href="...">标题</a></td>
#   <td>发送人</td>
#   <td>时间</td>
# </tr>
tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
trs = tr_pattern.findall(html)

print(f"\n匹配到 {len(trs)} 个 tr。前 10 个含 show-Message 的 tr 解析:")
count = 0
for tr in trs:
    if "show-Message" in tr:
        count += 1
        # 用正则提取里面的 td
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
        clean_tds = []
        for td in tds:
            # 清理 td 里的 HTML 标签和多余空白
            c = re.sub(r'<[^>]+>', '', td).strip()
            c = re.sub(r'\s+', ' ', c)
            clean_tds.append(c)
        print(f"Row {count}: {clean_tds}")
        if count >= 10:
            break
