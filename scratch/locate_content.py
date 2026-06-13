import re

# 我们来查找 "物理作业：圆周运动" 后面的内容
with open("scratch/msg_detail.html", "r", encoding="utf-8") as f:
    msg = f.read()

print("--- 消息详情 HTML 结构定位 ---")
# 我们可以搜索 "物理作业：圆周运动" 并输出前后的 1000 字符
idx = msg.find("物理作业：圆周运动")
if idx != -1:
    start = max(0, idx - 200)
    end = min(len(msg), idx + 2000)
    print("Found around '物理作业：圆周运动':")
    print(msg[start:end])
else:
    print("未在 msg_detail.html 中找到标题")


print("\n--- 纪律卫生详情 HTML 结构定位 ---")
with open("scratch/hygiene_detail.html", "r", encoding="utf-8") as f:
    hygiene = f.read()

# 纪律卫生里面有 7106 或者 "电扇未关"
idx_h = hygiene.find("电扇未关（提醒，现已关）")
if idx_h == -1:
    idx_h = hygiene.find("7106")
if idx_h != -1:
    start = max(0, idx_h - 200)
    end = min(len(hygiene), idx_h + 2000)
    print("Found around keyword in hygiene:")
    print(hygiene[start:end])
else:
    print("未在 hygiene_detail.html 中找到关键字")
