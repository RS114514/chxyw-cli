import re

with open("scratch/duty.html", "r", encoding="utf-8") as f:
    html = f.read()

# 找出所有的 <ul class="list-group" ...> 及其内部的 li
# 我们打印出前 5 个 block 里的 ul class 和 li 的 class 看看有什么区别
ul_blocks = re.findall(r'<ul[^>]+class=["\'](.*?)["\'](.*?)</ul>', html, re.DOTALL)
print(f"找到 {len(ul_blocks)} 个 ul 标签。")

# 让我们找出所有的 <li ...> 标签看看它们的 class
# 我们可以打印出所有 li 标签的 class，看看有没有不一样的
all_lis = re.findall(r'<li[^>]+class=["\'](.*?)["\']', html)
classes_cnt = {}
for c in all_lis:
    classes_cnt[c] = classes_cnt.get(c, 0) + 1

print("\nli 标签的 Class 统计:")
for c, count in classes_cnt.items():
    print(f"  Class: {repr(c)} -> Count: {count}")

# 有没有带有 style 或者是 background-color 的 li 或者 div 标签？
style_matches = re.findall(r'style=["\'](.*?)["\']', html)
print(f"\n找到 {len(style_matches)} 个 style 属性。它们的内容 (前 20 个):")
for s in set(style_matches)[:20]:
    print(f"  {s}")
