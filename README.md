# 春晖中学校园网命令行工具 (chunhui-cil)

[![Platform-Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/RS114514/chunhui-cil/releases/tag/latest)
[![Platform-macOS](https://img.shields.io/badge/platform-macOS-lightgrey)](https://github.com/RS114514/chunhui-cil/releases/tag/latest)
[![Language-Python](https://img.shields.io/badge/language-Python-3776AB)](https://www.python.org/)
[![License-MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/RS114514/chunhui-cil/blob/main/LICENSE)

本项目是专为春晖中学校园网打造的命令行工具（CLI）。无需打开浏览器，即可在终端高效完成邮件查阅、附件下载、值周安排检索、纪律卫生扣分查询、以及文件的寄存与分片上传。

本项目完全采用 Python 标准库实现，**零外部依赖**，具备极佳的兼容性与运行效率。

---

## 🚀 核心功能

*   **🔑 会话登录 (`login`)**
    *   支持校园网账号密码登录，自动识别并提示输入验证码。
    *   登录成功后，Cookie 会话将加密/持久化于本地，后续操作均无需重复登录。
*   **✉️ 收件箱管理 (`messages`)**
    *   查看收件箱通知列表。
    *   支持查看单条消息详情，正文中的 HTML 链接将自动转化为可读的锚文本格式展示。
    *   **智能附件解析**：自动匹配通知中关联的课件、压缩包或文档等附件。
    *   **一键附件下载**：支持一键将特定消息的附件下载至本地，并可自定义保存目录（支持自动创建不存在的路径）。
*   **📄 文章资讯与公告 (`news`)**
    *   支持阅读新闻聚焦(13), 校内公示(19), 值周小结(51)等不同文章栏目的列表，并支持自定义栏目 ID。
    *   支持在终端直观查阅文章具体正文排版，附带的文档、表格及附件超链接自动保留为可复制形式。
*   **🧹 纪律卫生查询 (`hygiene`)**
    *   快速检索全校或特定班级的纪律卫生考评打分记录。
    *   支持按页、按详情查询具体扣分项与考评时间。
*   **🏠 寝室与卫生考评 (`bedroom`)**
    *   **班级寝室检索**：一键获取特定班级分配使用的全部寝室房号。
    *   **宿舍楼宇考评**：支持对各栋宿舍楼宇（如 1=3号楼，3=5号楼，9=1号楼等）进行指定日期范围内的卫生与纪律考评打分汇总查询，支持仅过滤显示有扣分项 of 寝室。
*   **📅 值周排班检索 (`duty`)**
    *   **当前周高亮**：默认模式下一键高亮输出当前星期的行政值周、组员以及值周班级。
    *   **全局值周表**：支持使用 `--all` 列出整个学期所有周次的值周总表。
    *   **模糊搜索**：支持使用 `--search` 模糊搜索特定的教师名字或班级。
*   **🔍 失物招领查询 (`lostfound` / `lf`)**
    *   实时检索全校范围内的物品丢失或捡到进展登记表。
    *   阅读招领项目明细，展示描述、发布处及联系方式等信息。
*   **📁 文件存取寄取 (`file`)**
    *   **分片上传 (`file upload`)**：将本地任意文件以 100MB 为大小进行逻辑分片，手写 `multipart/form-data` 数据编码安全上传，并在上传完成后自动向服务器请求合并，返回 6 位数文件提取密码。
    *   **安全提取 (`file download`)**：凭 6 位数提取密码，安全高速地将寄存文件下载回本地，并可指定保存目录。

---

## 🛠️ 安装与使用

### 1. 环境准备
确保您的系统安装了 Python 3 (建议 3.6+)。无需安装任何第三方库（如 `requests` 或 `beautifulsoup4`），直接运行即可。

### 2. 账号登录
首次使用时需要登录以初始化本地会话：
```bash
python3 ch_cli.py login
```
系统会提示您输入用户名、密码以及终端展示的图形验证码（验证码字符会以字符画形式在终端显示，或提示其他简易输入方式）。

### 3. 命令指南

#### 📨 收件箱通知
*   **查看消息列表**：
    ```bash
    python3 ch_cli.py messages
    ```
*   **查看单条消息详情**：
    ```bash
    python3 ch_cli.py messages --show <消息ID>
    ```
*   **下载消息附带的全部附件**：
    ```bash
    python3 ch_cli.py messages --show <消息ID> --download
    ```
*   **自定义附件下载目录**（如保存至 `./downloads` 目录）：
    ```bash
    python3 ch_cli.py messages --show <消息ID> --download --out ./downloads
    ```

#### 📄 文章资讯与公告
*   **查看默认文章列表**（默认展示 19-校内公示）：
    ```bash
    python3 ch_cli.py news
    ```
*   **查看指定栏目的文章列表**（例如查看 13-新闻聚焦）：
    ```bash
    python3 ch_cli.py news --column 13
    ```
*   **阅读文章详情与附件链接**：
    ```bash
    python3 ch_cli.py news --show <文章ID>
    ```

#### 🧹 纪律卫生
*   **查看考评列表**：
    ```bash
    python3 ch_cli.py hygiene
    ```
*   **查看指定考评明细**：
    ```bash
    python3 ch_cli.py hygiene --show <考评ID>
    ```

#### 🏠 寝室与卫生考评
*   **查询班级使用的寝室分配**（如查询高一 10 班，年级: 1=高一, 2=高二, 3=高三）：
    ```bash
    python3 ch_cli.py bedroom class 1 10
    ```
*   **查询宿舍楼宇考评表**（如查询 3 号楼，默认过滤只显示有扣分记录的寝室）：
    ```bash
    python3 ch_cli.py bedroom hygiene 1
    ```
*   **显示该楼宇全部宿舍（包括未扣分宿舍）**：
    ```bash
    python3 ch_cli.py bedroom hygiene 1 --all
    ```
*   **指定日期范围查询**：
    ```bash
    python3 ch_cli.py bedroom hygiene 1 --start 2026-06-01 --end 2026-06-13
    ```

#### 📅 值周排班
*   **查看当前周值周详情**（高亮显示）：
    ```bash
    python3 ch_cli.py duty
    ```
*   **显示完整值周表**：
    ```bash
    python3 ch_cli.py duty --all
    ```
*   **按教师或班级检索**：
    ```bash
    python3 ch_cli.py duty --search <教师姓名/班级名称>
    ```

#### 🔍 失物招领
*   **查看最新登记的失物招领列表**（支持别名 `lf`）：
    ```bash
    python3 ch_cli.py lostfound
    # 或使用别名
    python3 ch_cli.py lf
    ```
*   **查看具体招领联系人及文字描述详情**：
    ```bash
    python3 ch_cli.py lf --show <登记ID>
    ```

#### 📁 文件寄存与下载
*   **寄存上传本地文件**：
    ```bash
    python3 ch_cli.py file upload <文件路径>
    ```
    上传成功后，终端将输出 6 位数的提取密码（例如：`123456`）。
*   **使用提取码下载寄存文件**：
    ```bash
    python3 ch_cli.py file download <提取密码> [--out <保存目录>]
    ```

---

## 💻 独立运行免环境版（自带 Python 运行时）

本项目支持在免 Python 环境依赖的 Windows/macOS 主机上直接开箱即用：

### 1. 绿色便携版（推荐，百分百内置独立 Python 运行时）
本版本专为没有安装任何 Python 解释器、且可能缺少 MSVC++ 运行依赖库的 Windows 主机设计。它直接封装了官方纯净的嵌入式 Python 运行时解释器，防误报且 100% 独立于系统环境。
- 前往 GitHub 仓库的 **Releases**（发布）页面。
- 在最新的 `Latest Release` 下，直接下载 **`chunhui-cil-portable.zip`**。
- 将压缩包完整解压至任意目录，双击或在命令行中运行目录下的 `chunhui-cil.bat` 即可直接使用：
  ```cmd
  chunhui-cil.bat messages
  ```

### 2. 单文件版 
- **Windows 用户**：前往 GitHub 仓库的 **Releases** 页面，直接下载 **`chunhui-cil.exe`** 即可。
- **macOS 用户**：下载 **`chunhui-cil-mac.zip`**，解压后在终端下直接运行 `chunhui-cil` 可执行程序即可。

### 3. 在本地手动打包
若要在本地电脑上自行打包：
1. 安装 PyInstaller 工具：
   ```bash
   pip install pyinstaller
   ```
2. 执行打包指令：
   ```bash
   pyinstaller --onefile --name chunhui-cil ch_cli.py
   ```
3. 打包完成后，即可在 `dist/` 目录下得到生成的可执行程序。

---

## ⚙️ 网络健壮性说明
*   本工具在底层 `make_request()` 请求中嵌入了 `10 秒` 超时防护。
*   针对校园网偶发的 `502 Bad Gateway` 或 `504 Gateway Timeout` 异常，内置了最多 `3 次` 的自动延迟重试机制，大幅提升了在网络不稳定环境下的运行成功率。

---

## 📅 版本更新与演进

### 🔄 重构对比：当前版本 vs 初代版本

为了解决初代版本中界面粗糙、数据解析混乱、网络稳定性差等局限，我们对项目进行了彻底的架构重构。以下是当前最新版本（v1.2.0）与最早原始版本的核心对比：

| 维度 | 初代版本 (原始纯文本) | 当前版本 (重构优化版) |
| :--- | :--- | :--- |
| **表格与排版** | 输出为未经处理的原始纯文本，中英文混排时表格线严重错位、歪歪扭扭。 | 引入基于 `unicodedata.east_asian_width` 的 `get_visual_width` 自适应视觉宽度算法，配合等宽字体，输出像素级对齐的完美 Markdown 表格。 |
| **会话与登录** | 每次运行命令均需重复输入账号密码登录，无本地持久化。 | 支持会话 Cookie 本地加密与持久化存储，登录一次即可自动复用，并具备在线状态自动心跳校验。 |
| **命令交互** | 参数解析极其简易，无分组，无命令帮助提示，容易输入错误。 | 重构了参数解析逻辑，新增详尽的命令指南与帮助信息，支持通过教师或班级姓名进行模糊搜索。 |
| **终端导航** | 仅支持简单的命令行输入，没有任何交互式界面。 | 引入无缓冲 `os.read` 箭头键捕获机制，支持跨平台 TUI 菜单导航，终端操作更加直观流畅。 |
| **附件与媒体** | 仅能查看文本内容，通知公告中附带的课件、压缩包等附件无法下载。 | 自动解析 HTML 正文中的附件链接，支持一键将消息/资讯中的所有附件下载至自定义本地目录。 |
| **文件寄取** | 无分片上传逻辑，大文件上传极易超时失败。 | 采用纯 Python 标准库手写 `multipart/form-data` 数据编码，支持 100MB 逻辑分片上传与智能合并，生成 6 位安全提取码，支持高速断点续传。 |
| **网络健壮性** | 遇到校园网偶发的 502/504 错误时会直接崩溃闪退。 | 底层 `make_request` 嵌入 10 秒超时防护，并支持最多 3 次延迟自动重试机制。 |
| **运行与分发** | 必须在本地安装 Python 3 环境及相关依赖，对普通用户门槛较高。 | 提供无需安装 Python 的单文件版可执行程序，以及内置独立 Python 运行时的 `chunhui-cil-portable.zip` 绿色便携包，解压即用。 |

---

### [v1.2.0] - 2026-06-17
#### 🎨 核心解析器与分片优化
- **分片大小规范化**：将文件分片上传的大小统一调整并锁定为 **100MB**，优化了分片合并请求的可靠性，避免大文件上传失败。
- **表格对齐算法**：在底层 `HTMLToMarkdown` 解析器中引入了基于中英文真实视觉宽度计算的等宽空格填充，彻底解决终端中表格错位问题。
- **协议补充**：补充了 MIT 开源授权协议文件 `LICENSE`，并在 README.md 中添加了跨平台运行徽标（Badges）和免 Python 依赖的可执行文件获取引导。

---

## 📄 开源协议

本项目基于 **[MIT License](LICENSE)** 协议开源。
