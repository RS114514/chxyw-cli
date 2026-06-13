import re

with open("scratch/msg_79123.html", "r", encoding="utf-8") as f:
    html = f.read()

# 查找 ArticleContent
content_m = re.search(r'<div class="ArticleContent[^>]*>(.*?)</div>', html, re.DOTALL)
if content_m:
    print("--- ArticleContent 原始内容 ---")
    print(repr(content_m.group(1).strip()))
    print("---------------------------------")
else:
    print("没有找到 ArticleContent")

# 另外，我们查找下整个 html 里所有的 a 标签超链接
links = re.findall(r'<a[^>]+href=["\'](.*?)["\'](.*?)>(.*?)</a>', html, re.DOTALL)
print("\n页面中的所有 a 超链接 (前20个):")
for l in links[:20]:
    href = l[0].strip()
    text = re.sub(r'<[^>]+>', '', l[2]).strip()
    print(f"  Href: {href} -> Text: {text}")
