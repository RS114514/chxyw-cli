import urllib.request
import http.cookiejar
import os
import time

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

# Use a standard browser User-Agent
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

url_login_page = "http://10.181.200.3/account/login/"
url_captcha = "http://10.181.200.3/account/create_code_img2/"

print("1. Accessing login page...")
try:
    req_login = urllib.request.Request(url_login_page)
    req_login.add_header("User-Agent", ua)
    with urllib.request.urlopen(req_login) as response:
        print(f"Login page response: {response.status}")
except Exception as e:
    print(f"Error accessing login page: {e}")

print("Cookies after accessing login page:")
for cookie in cj:
    print(f"  {cookie.name} = {cookie.value}")

print("\nWaiting 1 second...")
time.sleep(1)

print("\n2. Downloading captcha...")
try:
    req_captcha = urllib.request.Request(url_captcha)
    req_captcha.add_header("User-Agent", ua)
    with urllib.request.urlopen(req_captcha) as response:
        print(f"Captcha response: {response.status}")
        data = response.read()
        os.makedirs("scratch", exist_ok=True)
        with open("scratch/captcha.png", "wb") as f:
            f.write(data)
        print(f"Captcha image saved to scratch/captcha.png, size: {len(data)} bytes")
except Exception as e:
    print(f"Error downloading captcha: {e}")

print("Cookies after downloading captcha:")
for cookie in cj:
    print(f"  {cookie.name} = {cookie.value}")
