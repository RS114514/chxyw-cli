import re

log_path = "/Users/dop/.gemini/antigravity-ide/brain/17fbf9b1-907f-4557-800d-e3eadc5a2e81/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    text = f.read()

# 找出所有形如 "/xxxx/yyyy" 的字符串，它们可能是 API 路径
# 寻找跟校园网相关的 URL 路径
urls = set(re.findall(r'/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+/', text))
print("可能用到的 API 路径:")
for url in sorted(urls):
    print(f"  {url}")

# 也可以专门搜索 "make_request" 或 "/subjectArrangement" 等前缀
print("\n搜索具体的 make_request 相关的行:")
lines = text.split('\n')
for line in lines:
    if "make_request" in line and ("schedule" in line or "class" in line or "grade" in line):
        # 截取一部分打印
        idx = line.find("make_request")
        print(line[max(0, idx - 100):min(len(line), idx + 200)])
