with open("scratch/msg_list.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
matches = re.findall(r'(附件|paperclip|clip|file|download|zip|pdf|doc|xls|ppt|png|jpg|txt|rar)', html, re.IGNORECASE)
print("在 msg_list.html 中匹配到的关键字个数:", len(matches))
print("去重后的匹配关键字:", set(matches))

links = re.findall(r'href=["\'](.*?)["\']', html)
other_links = [l for l in links if "show-Message" not in l and "brower-Others-Information" not in l]
print("\n列表页中其他超链接:")
for l in list(set(other_links))[:20]:
    print(f"  {l}")
