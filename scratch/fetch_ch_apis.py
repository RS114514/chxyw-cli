import sys
import os

# 将 /Users/dop/Desktop/RS 加入 sys.path 以便导入 ch_cli
sys.path.append("/Users/dop/Desktop/RS")
from ch_cli import make_request

def grab_and_save(url, filename):
    print(f"正在抓取 {url} ...")
    status, body, _ = make_request(url, method="GET")
    if status == 200:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(body.decode("utf-8", errors="ignore"))
        print(f"成功保存至 {filename} (大小: {len(body)} 字节)")
    else:
        print(f"抓取 {url} 失败: HTTP Code {status}")

grab_and_save("/fileaccess/show-AccessInterface/", "scratch/file_interface.html")
grab_and_save("/classappraise/TeacherDutyWeek_JustForView/", "scratch/duty.html")
