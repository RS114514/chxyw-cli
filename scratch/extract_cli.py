import json

log_path = "/Users/dop/.gemini/antigravity-ide/brain/17fbf9b1-907f-4557-800d-e3eadc5a2e81/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

step_173_content = None
step_185_target = None
step_185_replacement = None

for line in lines:
    try:
        obj = json.loads(line)
        if obj.get("type") == "PLANNER_RESPONSE":
            for tc in obj.get("tool_calls", []):
                args = tc.get("args", {})
                step = obj.get("step_index")
                if step == 173:
                    step_173_content = args.get("ReplacementContent")
                elif step == 185:
                    step_185_target = args.get("TargetContent")
                    step_185_replacement = args.get("ReplacementContent")
    except Exception as e:
        pass

if step_173_content:
    print("找到 Step 173 的 ReplacementContent，长度:", len(step_173_content))
    content = step_173_content
    if step_185_target and step_185_replacement:
        print("应用 Step 185 的替换...")
        if step_185_target in content:
            content = content.replace(step_185_target, step_185_replacement)
            print("替换成功。")
        else:
            print("警告: Step 185 的 TargetContent 未在内容中找到！")
            # 可能是因为有小的换行或空格差异，我们看看是否能强行替换
    
    # 写入 ch_cli.py
    with open("ch_cli.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("已成功还原 ch_cli.py！")
else:
    print("未找到 Step 173 的内容。")
