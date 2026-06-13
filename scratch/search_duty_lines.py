with open("scratch/duty.html", "r", encoding="utf-8") as f:
    html = f.read()

# 清除样式和脚本
import re
text = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)

lines = [line.strip() for line in text.split('\n') if line.strip()]

# 查找包含了“周次”或者包含“值周”或“行政”的行
print("包含相关词汇的行:")
for idx, line in enumerate(lines):
    if any(k in line for k in ["周次", "行政值周", "值周班级", "值周教师", "小组成员"]):
        print(f"Line {idx+1}: {line}")
        # 顺便把前后的几行也打一下
        start = max(0, idx - 2)
        end = min(len(lines), idx + 8)
        print("  上下文:")
        for k in range(start, end):
            print(f"    {k+1}: {lines[k]}")
        print("-" * 30)
