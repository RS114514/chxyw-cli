import urllib.request
import json
import os

url_msg_detail = "http://10.181.200.3/sitemessage/show-Message/80631/"
url_hygiene_detail = "http://10.181.200.3/classappraise/show-Message/1113/"

session_file = os.path.expanduser("~/.ch_cli_session.json")

with open(session_file, "r") as f:
    session = json.load(f)

sessionid = session.get("sessionid")
csrftoken = session.get("csrftoken")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

def fetch_and_save(url, filename):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8", errors="ignore")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(body)
            print(f"成功保存 {url} -> {filename}")
    except Exception as e:
        print(f"请求失败 {url}: {e}")

fetch_and_save(url_msg_detail, "scratch/msg_detail.html")
fetch_and_save(url_hygiene_detail, "scratch/hygiene_detail.html")
