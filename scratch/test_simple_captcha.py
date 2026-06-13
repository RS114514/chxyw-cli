import urllib.request

url_captcha = "http://10.181.200.3/account/create_code_img2/"
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

req = urllib.request.Request(url_captcha)
req.add_header("User-Agent", ua)

try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.status}")
        print(f"Content length: {len(response.read())}")
        for k, v in response.getheaders():
            print(f"Header: {k} = {v}")
except Exception as e:
    print(f"Error: {e}")
