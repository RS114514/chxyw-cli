import urllib.request
import urllib.parse
import http.cookiejar
import uuid
import time

# Create a cookie jar to track cookies automatically
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Install the opener globally
urllib.request.install_opener(opener)

url_get = "http://10.181.200.3/fileaccess/show-AccessInterface/"
url_upload = "http://10.181.200.3/fileaccess/files_upload/"
url_complete = "http://10.181.200.3/fileaccess/upload_complete/"

# 1. GET request to obtain cookies (csrftoken)
print("1. Sending GET to show-AccessInterface to get cookies...")
try:
    with urllib.request.urlopen(url_get) as response:
        print(f"GET Status: {response.status}")
        for cookie in cj:
            print(f"Cookie found: {cookie.name} = {cookie.value}")
except Exception as e:
    print(f"GET Error: {e}")

# Extract CSRF token
csrf_token = ""
for cookie in cj:
    if cookie.name == "csrftoken":
        csrf_token = cookie.value
        break

# 2. Upload chunk
task_id = "wu_" + uuid.uuid4().hex[:14]
filename = "test_cli.txt"
content = b"Hello from CLI!"
size_str = str(len(content))

print(f"\n2. Uploading chunk, Task ID: {task_id}")

boundary = uuid.uuid4().hex
data = []

# Standard fields
fields = {
    'id': 'WU_FILE_0',
    'name': filename,
    'type': 'text/plain',
    'lastModifiedDate': 'Mon Jun 15 2026 12:00:00 GMT+0800 (China Standard Time)',
    'size': size_str,
    'chunks': '1',
    'chunk': '0',
    'task_id': task_id,
}

if csrf_token:
    fields['csrfmiddlewaretoken'] = csrf_token

for name, val in fields.items():
    data.append(f"--{boundary}".encode('utf-8'))
    data.append(f'Content-Disposition: form-data; name="{name}"'.encode('utf-8'))
    data.append(b'')
    data.append(val.encode('utf-8'))

# File field
data.append(f"--{boundary}".encode('utf-8'))
data.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"'.encode('utf-8'))
data.append(b'Content-Type: text/plain')
data.append(b'')
data.append(content)

data.append(f"--{boundary}--".encode('utf-8'))
data.append(b'')

body = b'\r\n'.join(data)

req_upload = urllib.request.Request(url_upload, data=body)
req_upload.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
if csrf_token:
    req_upload.add_header('X-CSRFToken', csrf_token)
    req_upload.add_header('Referer', url_get)

try:
    with urllib.request.urlopen(req_upload) as response:
        print(f"Upload chunk status: {response.status}")
        print(f"Upload chunk response: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Upload chunk error: {e}")

time.sleep(1)

# 3. Complete upload
print("\n3. Completing upload...")
params_complete = {
    'task_id': task_id,
    'filename': filename
}
if csrf_token:
    params_complete['csrfmiddlewaretoken'] = csrf_token

data_complete = urllib.parse.urlencode(params_complete).encode('utf-8')

req_complete = urllib.request.Request(url_complete, data=data_complete)
if csrf_token:
    req_complete.add_header('X-CSRFToken', csrf_token)
    req_complete.add_header('Referer', url_get)

try:
    with urllib.request.urlopen(req_complete) as response:
        print(f"Complete status: {response.status}")
        print(f"Complete response: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Complete error: {e}")
