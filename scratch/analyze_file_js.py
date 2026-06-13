import re

with open("scratch/file_interface.html", "r", encoding="utf-8") as f:
    html = f.read()

# 找出所有的 script 块
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"共有 {len(scripts)} 个 script 块。")

# 寻找含有上传或者下载关键字的段落
for i, s in enumerate(scripts):
    if any(k in s for k in ["files_upload", "upload_complete", "get-AccessFile", "receive-AccessFile", "AccessFile"]):
        print(f"\n--- Script {i} (包含关键字) ---")
        lines = s.split('\n')
        # 打印部分代码
        for j, line in enumerate(lines):
            if any(k in line for k in ["files_upload", "upload_complete", "get-AccessFile", "receive-AccessFile", "AccessPass", "Pass"]):
                # 打印该行前后的 5 行
                start = max(0, j - 4)
                end = min(len(lines), j + 10)
                print(f"Match around line {j+1}:")
                print('\n'.join(lines[start:end]))
                print("-" * 20)
