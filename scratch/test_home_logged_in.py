import urllib.request
import urllib.parse
import os
import re

url_home = "http://10.181.200.3/home/index/"
sessionid = "g2j7ag8ni4bxb7hab8hpnibjwad4kkmd"
csrftoken = "zpohY7L55UqlXJxlK2XhhwFJx1Es7oge"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

req = urllib.request.Request(url_home, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.status}")
        body = response.read().decode("utf-8", errors="ignore")
        print(f"Body size: {len(body)}")
        print("Body content:")
        print(body)
        
        # Let's search for "account/logout" or user names
        match_logout = re.search(r'href=["\']/account/logout/["\']', body)
        if match_logout:
            print("Found logout link in HTML!")
            
        # Let's find any text in the top navigation bar where the login button was
        # Usually lines around the profile dropdown
        # Let's find all text inside <li class="nav-item dropdown"> ... </li>
        dropdowns = re.findall(r'<li class="nav-item dropdown">(.*?)</li>', body, re.DOTALL)
        for i, dropdown in enumerate(dropdowns):
            clean = re.sub(r'<[^>]+>', '', dropdown).strip()
            clean = re.sub(r'\s+', ' ', clean)
            print(f"Dropdown {i}: {clean}")
            
except Exception as e:
    print(f"Error: {e}")
