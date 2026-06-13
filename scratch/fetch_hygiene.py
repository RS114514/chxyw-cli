import urllib.request
import json
import os

url_hygiene = "http://10.181.200.3/classappraise/hygienePictures_receive_list/"
session_file = os.path.expanduser("~/.ch_cli_session.json")

with open(session_file, "r") as f:
    session = json.load(f)

sessionid = session.get("sessionid")
csrftoken = session.get("csrftoken")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

req = urllib.request.Request(url_hygiene, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.status}")
        body = response.read().decode("utf-8", errors="ignore")
        print(f"Body size: {len(body)}")
        with open("scratch/hygiene_list.html", "w", encoding="utf-8") as f:
            f.write(body)
        print("已将纪律卫生列表 HTML 保存到 scratch/hygiene_list.html")
except Exception as e:
    print(f"请求失败: {e}")
