with open("scratch/duty.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
blocks = re.findall(r'<ul class="list-group"\s*>(.*?)</ul>', html, re.DOTALL)

for i, block in enumerate(blocks):
    if "list-group-item-success" in block:
        print(f"Block {i} 包含 list-group-item-success:")
        lis = re.findall(r'<li[^>]*>(.*?)</li>', block, re.DOTALL)
        for j, li in enumerate(lis):
            # 提取这一行 li 标签的 class 和清洁内容
            li_class = ""
            class_m = re.search(r'class=["\'](.*?)["\']', html) # 我们可以在 block 里找
            # 为了准确，我们正则匹配 <li ...> 这一整行
            print(f"  Li {j+1}: {re.sub(r'<[^>]+>', '', li).strip()}")
