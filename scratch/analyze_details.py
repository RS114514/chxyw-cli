import re

def clean_html(text):
    # 去除样式和脚本
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    # 替换 <br> 等为换行
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n', text, flags=re.IGNORECASE)
    # 去除其他 HTML 标签
    text = re.sub(r'<[^>]+>', '', text)
    # 解码一些常见 entity
    text = text.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    # 去除连续空行，整理格式
    lines = [line.strip() for line in text.split('\n')]
    non_empty = []
    for line in lines:
        if line:
            non_empty.append(line)
        elif not non_empty or non_empty[-1] != "":
            non_empty.append("")
    return '\n'.join(non_empty).strip()

print("--- 消息详情分析 ---")
with open("scratch/msg_detail.html", "r", encoding="utf-8") as f:
    msg_html = f.read()

# 寻找消息的标题、发件人、时间、内容。
# 在 HTML 中通常有特定的 div 或 class。我们可以把核心部分提取出来。
# 例如，搜索 <h4> 或 <h3>，或是寻找消息标题
title_m = re.search(r'<h[1-6][^>]*>(.*?)</h[1-6]>', msg_html, re.DOTALL)
if title_m:
    print(f"Title: {clean_html(title_m.group(1))}")

# 让我们看看所有可能包含发送者/时间的文本
# 我们可以打印出前 30 行非空的清理文本，来看看结构
cleaned_msg = clean_html(msg_html)
print("清理后的部分文本:")
for i, line in enumerate(cleaned_msg.split('\n')[:25]):
    print(f"{i}: {line}")


print("\n--- 纪律卫生详情分析 ---")
with open("scratch/hygiene_detail.html", "r", encoding="utf-8") as f:
    hygiene_html = f.read()

# 类似地，我们看一下纪律卫生的清理文本
cleaned_hygiene = clean_html(hygiene_html)
print("清理后的部分文本:")
for i, line in enumerate(cleaned_hygiene.split('\n')[:25]):
    print(f"{i}: {line}")

# 我们也要看一下图片/视频的链接。纪律卫生可能包含照片。
# 在 HTML 源码中搜索 img 标签或 video 标签，或者 src="...jpg" 
imgs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', hygiene_html)
print("\n图片链接:")
for img in imgs:
    print(f"  {img}")

videos = re.findall(r'<video[^>]+src=["\'](.*?)["\']', hygiene_html)
print("\n视频链接:")
for vid in videos:
    print(f"  {vid}")
