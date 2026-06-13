import re

with open("scratch/duty.html", "r", encoding="utf-8") as f:
    html = f.read()

# 每个卡片被包含在 <div id="TeacherDutyArrangementForID... >
# ...
# </div> 之间。
# 我们可以直接匹配 <ul class="list-group" > 到 </ul> 之间的块
blocks = re.findall(r'<ul class="list-group"\s*>(.*?)</ul>', html, re.DOTALL)
print(f"解析到 {len(blocks)} 个值周配置块。")

duties = []
for block in blocks:
    # 提取周次状态 (当前/过去/将来)
    status = "未知"
    if "<!--当前周次-->" in block:
        status = "当前"
    elif "<!--过去周次-->" in block:
        status = "过去"
    elif "<!--将来周次-->" in block:
        status = "将来"
        
    # 提取 li 标签列表
    lis = re.findall(r'<li[^>]*>(.*?)</li>', block, re.DOTALL)
    if not lis:
        continue
        
    # 第一个 li 是周次名称，可能会有 <b> 标签
    week_name = re.sub(r'<[^>]+>', '', lis[0]).strip()
    date_range = re.sub(r'<[^>]+>', '', lis[1]).strip() if len(lis) > 1 else ""
    
    # 解析其他细节
    details = {}
    for li in lis[2:]:
        clean = re.sub(r'<[^>]+>', '', li).strip()
        if "：" in clean:
            k, v = clean.split("：", 1)
            details[k.strip()] = v.strip()
        else:
            # 兼容一些没有分号的行
            details[clean] = ""
            
    duties.append({
        "status": status,
        "week": week_name,
        "date": date_range,
        "admin": details.get("行政值周", ""),
        "group1": details.get("第一小组", ""),
        "group2": details.get("第二小组", ""),
        "group3": details.get("第三小组", ""),
        "class": details.get("值周班级", ""),
        "talk": details.get("旗下讲话", "")
    })

print(f"成功提取了 {len(duties)} 条值周信息。")
print("\n--- 提取样本 (前3个) ---")
for d in duties[:3]:
    print(d)

print("\n--- 当前周次 ---")
for d in duties:
    if d["status"] == "当前":
        print(d)
