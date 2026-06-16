import urllib.request
import urllib.parse
import json

IP_PORT = "10.181.201.188:5000"
TOKEN = "zmwdE4vqUthmo"

def make_get_request(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status, resp.read().decode('utf-8')
    except Exception as e:
        return 0, str(e)

def test():
    print("=== 开始群晖相册 API 深入探测 ===")
    
    # 1. 获取文件夹列表
    # 尝试两个网关
    gateways = [
        f"http://{IP_PORT}/photo/webapi/entry.cgi",
        f"http://{IP_PORT}/webapi/entry.cgi"
    ]
    
    folders = []
    for gw in gateways:
        params = {
            "api": "SYNO.FotoTeam.Browse.Folder",
            "method": "list",
            "version": 1,
            "SynoToken": TOKEN,
            "offset": 0,
            "limit": 100,
            "id": 1,
            "additional": '["thumbnail"]'
        }
        url = f"{gw}?{urllib.parse.urlencode(params)}"
        print(f"\n[尝试网关 Folder] {gw} ...")
        status, body = make_get_request(url)
        if status == 200:
            try:
                res = json.loads(body)
                if res.get("success"):
                    folders = res.get("data", {}).get("list", [])
                    print(f"✅ 成功！获取到 {len(folders)} 个共享文件夹")
                    for f in folders[:5]:
                        print(f"  - ID: {f.get('id')}, Name: {f.get('name')}")
                    break
                else:
                    print(f"❌ 失败: API 返回 success=false, error={res.get('error')}")
            except Exception as e:
                print(f"❌ 失败: 解析 JSON 异常: {e}")
        else:
            print(f"❌ 失败: HTTP Code {status}, 错误: {body}")
            
    if not folders:
        print("无法获取任何文件夹列表，探测终止。")
        return
        
    # 2. 对每个文件夹获取照片列表
    # 尝试两种网关和两种 API
    # 我们拿第一个文件夹作为测试目标
    target_folder = folders[0]
    fid = target_folder.get("id")
    fname = target_folder.get("name")
    print(f"\n选择测试文件夹: {fname} (ID: {fid})")
    
    test_cases = [
        # (网关, API)
        (f"http://{IP_PORT}/photo/webapi/entry.cgi", "SYNO.FotoTeam.Browse.Item"),
        (f"http://{IP_PORT}/webapi/entry.cgi", "SYNO.FotoTeam.Browse.Item"),
        (f"http://{IP_PORT}/photo/webapi/entry.cgi", "SYNO.Foto.Browse.Item"),
        (f"http://{IP_PORT}/webapi/entry.cgi", "SYNO.Foto.Browse.Item"),
    ]
    
    for gw, api in test_cases:
        params = {
            "api": api,
            "method": "list",
            "version": 1,
            "SynoToken": TOKEN,
            "offset": 0,
            "limit": 100,
            "folder_id": fid,
            "additional": '["thumbnail", "resolution"]'
        }
        url = f"{gw}?{urllib.parse.urlencode(params)}"
        print(f"\n[测试照片 API] 网关: {gw} | API: {api} ...")
        status, body = make_get_request(url)
        if status == 200:
            try:
                res = json.loads(body)
                if res.get("success"):
                    items = res.get("data", {}).get("list", [])
                    print(f"✅ 成功！在该文件夹下获取到 {len(items)} 张照片")
                    if items:
                        print(f"  首条照片数据: {json.dumps(items[0], ensure_ascii=False)}")
                else:
                    print(f"❌ 失败: API 返回 success=false, error={res.get('error')}")
            except Exception as e:
                print(f"❌ 失败: 解析 JSON 异常: {e}")
        else:
            print(f"❌ 失败: HTTP Code {status}, 错误: {body}")

if __name__ == "__main__":
    test()
