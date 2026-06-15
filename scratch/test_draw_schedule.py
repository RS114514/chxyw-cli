import sys
import os
import json
import re

# 将父目录加入 path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ch_cli import draw_schedule_table

def main():
    html_path = os.path.join(os.path.dirname(__file__), "schedule_1_1.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    match = re.search(r'dataObj\s*=\s*(\[\[.*?\]\])\s*;', html_content)
    if not match:
        print("未在 html 中找到 dataObj")
        return
        
    data_obj = json.loads(match.group(1))
    
    # 模拟加入超长课程名，以测试自适应截断效果
    data_obj[1][1] = "非常长非常长非常长的课程名称带各种文字括号"
    # 模拟列数不对的情况，测试动态列宽
    data_obj[0].append("星期六")
    data_obj[1].append("测试周末课")
    
    print("--- 渲染课表测试开始 ---")
    draw_schedule_table(data_obj)
    print("--- 渲染课表测试结束 ---")

if __name__ == "__main__":
    main()
