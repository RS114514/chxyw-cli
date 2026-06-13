import json

log_path = "/Users/dop/.gemini/antigravity-ide/brain/17fbf9b1-907f-4557-800d-e3eadc5a2e81/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    try:
        obj = json.loads(line)
        if obj.get("type") == "PLANNER_RESPONSE":
            for tc in obj.get("tool_calls", []):
                args = tc.get("args", {})
                step = obj.get("step_index")
                if step == 163:
                    content = args.get("CodeContent", "")
                    print(f"Step 163 CodeContent 长度: {len(content)}")
                    print("前 200 字符:\n", content[:200])
                    print("后 200 字符:\n", content[-200:])
                    
                    # 写入临时文件以供查看
                    with open("scratch/step_163.py", "w", encoding="utf-8") as f_out:
                        f_out.write(content)
                    print("已将 Step 163 的内容写入 scratch/step_163.py")
    except Exception as e:
        pass
