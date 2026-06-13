import urllib.request
import json
import os

url_file = "http://10.181.200.3/fileaccess/show-AccessInterface/"
session_file = os.path.expanduser("~/.ch_cli_session.json")

with open(session_file, "r") as f:
    session = json.load(f)

sessionid = session.get("sessionid")
csrftoken = session.get("csrftoken")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

req = urllib.request.Request(url_file, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8", errors="ignore")
        with open("scratch/file_interface.html", "w", encoding="utf-8") as f:
            f.write(body)
        print("已成功保存文件存取页面 HTML 到 scratch/file_interface.html")
except Exception as e:
    print(f"抓取失败: {e}")
