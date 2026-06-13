with open("scratch/msg_detail.html", "r", encoding="utf-8") as f:
    msg = f.read()

# 找出所有包含 "物理作业：圆周运动" 的位置
idxs = [i for i in range(len(msg)) if msg.startswith("物理作业：圆周运动", i)]
print("Indices of keyword:", idxs)

for idx in idxs:
    print(f"\n--- Around index {idx} ---")
    start = max(0, idx - 150)
    end = min(len(msg), idx + 1500)
    print(msg[start:end])
