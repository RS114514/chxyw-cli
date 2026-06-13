import urllib.request
import re

url_msg = "http://10.181.200.3/sitemessage/message-Receive-list/"
sessionid = "g2j7ag8ni4bxb7hab8hpnibjwad4kkmd"
csrftoken = "zpohY7L55UqlXJxlK2XhhwFJx1Es7oge"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

req = urllib.request.Request(url_msg, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.status}")
        body = response.read().decode("utf-8", errors="ignore")
        print(f"Body size: {len(body)}")
        
        # Let's save body to file to analyze later
        with open("scratch/msg_list.html", "w", encoding="utf-8") as f:
            f.write(body)
        print("Saved HTML to scratch/msg_list.html")
        
        # Let's extract the table rows
        # Message rows are usually inside <tbody> or <tr> with some pattern
        # Let's count how many <tr> or <td> there are
        trs = re.findall(r'<tr>(.*?)</tr>', body, re.DOTALL)
        print(f"Total <tr> elements: {len(trs)}")
        for i, tr in enumerate(trs[:10]):
            clean = re.sub(r'<[^>]+>', ' ', tr).strip()
            clean = re.sub(r'\s+', ' ', clean)
            print(f"Row {i}: {clean}")
            
except Exception as e:
    print(f"Error: {e}")
