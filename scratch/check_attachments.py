import re

with open("scratch/msg_detail.html", "r", encoding="utf-8") as f:
    html = f.read()

# 查找所有 a 标签的 href
links = re.findall(r'<a[^>]+href=["\'](.*?)["\']', html)
print("消息详情里所有的超链接:")
for link in links:
    print(f"  {link}")

# 查找所有包含 "下载" 或 "文件" 或 "附件" 的文本及前后的 HTML
matches = re.finditer(r'(下载|文件|附件|file|download)', html, re.IGNORECASE)
print("\n关键字上下文匹配:")
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(html), m.end() + 100)
    print(f"[{m.group(0)}]: {repr(html[start:end])}")
    print("-" * 30)
