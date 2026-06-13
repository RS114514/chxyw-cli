import re

log_path = "/Users/dop/.gemini/antigravity-ide/brain/17fbf9b1-907f-4557-800d-e3eadc5a2e81/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    text = f.read()

# 寻找含有 ClassClassArrangement_JustForView 的行
lines = text.split('\n')
print("找到以下相关的 log 行:")
count = 0
for line in lines:
    if "ClassClassArrangement_JustForView" in line:
        count += 1
        print(f"Match {count}:")
        # 打印这一行前后的片段
        idx = line.find("ClassClassArrangement_JustForView")
        print(line[max(0, idx - 150):min(len(line), idx + 800)])
        print("-" * 40)
