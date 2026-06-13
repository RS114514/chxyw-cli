import re

with open("scratch/duty.html", "r", encoding="utf-8") as f:
    html = f.read()

# 清除样式和脚本
text = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)

lines = [line.strip() for line in text.split('\n') if line.strip()]
print(f"总共有 {len(lines)} 行非空文本。前 100 行展示:")
for idx, line in enumerate(lines[:100]):
    print(f"{idx+1:3d}: {line}")
