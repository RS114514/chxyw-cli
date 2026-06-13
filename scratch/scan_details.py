import re
import urllib.request
import json
import os

session_file = os.path.expanduser("~/.ch_cli_session.json")
with open(session_file, "r") as f:
    session = json.load(f)

sessionid = session.get("sessionid")
csrftoken = session.get("csrftoken")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

with open("scratch/msg_list.html", "r", encoding="utf-8") as f:
    html = f.read()

# 找出所有的消息 ID
msg_ids = re.findall(r'/sitemessage/show-Message/(\d+)/', html)
# 去重并排序
msg_ids = sorted(list(set(msg_ids)), reverse=True)

print(f"共发现 {len(msg_ids)} 个消息 ID。开始扫描前 30 个消息以查找潜在附件链接...")

found_attachments = []

for mid in msg_ids[:30]:
    url = f"http://10.181.200.3/sitemessage/show-Message/{mid}/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8", errors="ignore")
            # 搜索 body 里的 href 链接
            links = re.findall(r'href=["\'](.*?)["\']', body)
            # 寻找非通用的链接，比如含有 static, file, upload, download, media 等，或者常见后缀
            for link in links:
                link_clean = link.strip()
                if not link_clean or link_clean == "#" or "javascript:" in link_clean:
                    continue
                # 如果包含常见文件格式后缀或者包含 /fileaccess/ 或 /static/
                if any(ext in link_clean.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.rar', '.png', '.jpg']) or "/fileaccess/" in link_clean:
                    # 排除一些 Logo 之类的图片
                    if "Logo" in link_clean or "newFunc" in link_clean or "sydw" in link_clean:
                        continue
                    found_attachments.append((mid, link_clean))
                    print(f"消息 [ID: {mid}] 发现疑似附件链接: {link_clean}")
    except Exception as e:
        print(f"请求消息 {mid} 失败: {e}")

print(f"\n扫描完毕。共找到 {len(found_attachments)} 个附件链接:")
for mid, link in found_attachments:
    print(f"  Message {mid} -> {link}")
