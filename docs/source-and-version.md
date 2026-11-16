# 来源、版本与再生成

## 来源

本仓库内容提取自本机安装目录：

```text
C:\Program Files\conTEST 1.15\Documentation\ContinuousTesting Adapter
```

源站点是 DocFX 生成的 HTML 帮助。提取时共发现并转换 99 个 article 页面：

| 分类 | 页面数 |
| --- | ---: |
| general | 2 |
| gRPC | 34 |
| TCP/IP | 24 |
| Serial | 24 |
| MQTT | 12 |
| Digital I/O | 3 |

## 再生成

在装有 conTEST 1.15 的 Windows 机器、仓库根目录运行：

```powershell
C:\msys64\ucrt64\bin\python.exe tools\extract_contest_docs.py
```

脚本仅依赖 Python 标准库，会：

- 去除 DocFX 导航、CSS 和 JavaScript；
- 将 article 正文、表格和代码块转换为 Markdown；
- 生成 `reference/<Adapter>/*.md`；
- 从 gRPC Overview 的代码块提取 `protocol/grpc/CtGrpcRemote.proto`。

如果安装路径不同，使用 `--source`；需要临时对比而不覆盖仓库时使用 `--output`。

## 更新规则

1. 新版本放在独立分支或先生成到临时目录，不要默认覆盖 1.15 契约。
2. 对比消息 ID、proto field number、enum、topic、payload、许可证和行为说明。
3. 更新 README 的版本边界和已知缺页。
4. 运行链接与协议校验。
5. 只有连接真实 conTEST 并具备许可证后，才能把相关项目标记为 runtime verified。

## 源帮助中的不确定项

- TOC/Overview 引用了多个 Live Monitoring 页面，但此次安装目录没有对应独立 HTML 文件。
- Digital I/O 设备型号出现 `USB-5750`/`USB-4750` 不一致。
- gRPC Overview 说 proto 文件位于帮助旁边，但此次目录清单中没有独立 `.proto`；契约是从 Overview 内嵌代码块提取的。

这些问题已在 README 和 AGENTS 中显式保留，避免 agent 把缺页或拼写冲突解释成确定事实。
