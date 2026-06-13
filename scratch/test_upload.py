import urllib.request
import urllib.parse
import uuid
import time

url_upload = "http://10.181.200.3/fileaccess/files_upload/"
url_complete = "http://10.181.200.3/fileaccess/upload_complete/"

# Generate a WebUploader style task_id: e.g., wu_1g8o20u2n19k51
# Usually wu_ + 14 chars
task_id = "wu_" + uuid.uuid4().hex[:14]
filename = "test_cli.txt"
content = b"Hello from CLI!"
size_str = str(len(content))

print(f"Task ID: {task_id}")

# Construct multipart request with all standard WebUploader fields
boundary = uuid.uuid4().hex
data = []

fields = {
    'id': 'WU_FILE_0',
    'name': filename,
    'type': 'text/plain',
    'lastModifiedDate': 'Mon Jun 15 2026 12:00:00 GMT+0800 (China Standard Time)',
    'size': size_str,
    'chunks': '1',
    'chunk': '0',
    'task_id': task_id
}

for name, val in fields.items():
    data.append(f"--{boundary}".encode('utf-8'))
    data.append(f'Content-Disposition: form-data; name="{name}"'.encode('utf-8'))
    data.append(b'')
    data.append(val.encode('utf-8'))

# file field
data.append(f"--{boundary}".encode('utf-8'))
data.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"'.encode('utf-8'))
data.append(b'Content-Type: text/plain')
data.append(b'')
data.append(content)

data.append(f"--{boundary}--".encode('utf-8'))
data.append(b'')

body = b'\r\n'.join(data)

req = urllib.request.Request(url_upload, data=body)
req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')

try:
    with urllib.request.urlopen(req) as response:
        print(f"Upload chunk status: {response.status}")
        print(f"Upload chunk response: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Upload chunk error: {e}")

time.sleep(1)

# Complete upload
data_complete = urllib.parse.urlencode({
    'task_id': task_id,
    'filename': filename
}).encode('utf-8')

req_complete = urllib.request.Request(url_complete, data=data_complete)
try:
    with urllib.request.urlopen(req_complete) as response:
        print(f"Complete status: {response.status}")
        print(f"Complete response: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Complete error: {e}")
