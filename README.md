# 常用数学公式

按数学学科组织的中文 LaTeX 公式手册，涵盖基础数学、分析、代数、几何、拓扑、数论及概率统计。内容以定义、公式、定理、适用条件和误差估计为主，并附参考文献与可点击的公式及主题索引。

直接阅读：[完整 PDF](main.pdf)。

## 内容结构

全书目前分为 **8 篇、37 章**，具体顺序以 [main.tex](main.tex) 为准。

| 篇 | 章节 |
| --- | --- |
| 基础数学 | 初等数学、平面几何、立体几何、初等数论、高等代数、数学分析 |
| 逻辑、集合与离散数学 | 数理逻辑、集合论、离散数学、组合数学与图论 |
| 代数结构 | 群论、环论、域论、模论 |
| 拓扑、测度与分析 | 一般拓扑、测度论、实分析、复分析、泛函分析、凸分析、调和分析 |
| 方程、变分与动力系统 | 常微分方程、数值分析、变分法、偏微分方程、动力系统、分形分析 |
| 概率、统计与随机过程 | 概率论、数理统计、随机过程 |
| 高阶几何与拓扑 | 微分几何、代数拓扑、微分拓扑、代数几何 |
| 进阶数论 | 几何数论、解析数论、代数数论 |

## 仓库目录

```text
formula/
├── main.tex          # 全书入口、导言区与章节顺序
├── main.pdf          # 可直接阅读的完整成品
├── chapter/          # 按学科命名的章节源文件
├── cover/            # 封面及图片资源
├── preface/          # 前言
├── introduction/     # 引言
├── colophon/         # 尾页及图片资源
├── references.tex    # 参考文献
├── index.ist         # 中文拼音索引样式
├── build_book.py     # 编译与索引构建入口
├── Makefile          # make 构建入口
└── build/            # 本地编译产物，不纳入版本控制
```

## 编译

### 环境要求

- Python 3。
- TeX Live 或其他提供 `xelatex`、`latexmk` 与 `upmendex` 的完整 TeX 环境；这些命令需加入 `PATH`。
- 当前排版使用 `ctexbook` 的 `fontset=windows`，适合安装了 Windows 中文字体的环境。在其他系统上编译时，需要先在 `main.tex` 中调整字体配置。
- 文档使用 TikZ、tcolorbox、subfiles、hyperref 等宏包，并包含 EPS 图片；建议安装完整 TeX Live。当前本地使用 TeX Live 2024。

### 构建全书

在仓库根目录执行：

```sh
python build_book.py
```

脚本调用 XeLaTeX 与 latexmk，并使用 upmendex 按中文拼音生成索引。完整输出位于 `build/main.pdf`；首次编译需要多轮处理目录、交叉引用和索引。

需要强制重新构建时：

```sh
python build_book.py --force
```

也可以在安装了 Make 的环境中执行 `make`。

### 更新仓库中的 PDF

检查 `build/main.log`，确认交叉引用和索引完整，并检查 PDF 排版后，再将成品复制到仓库根目录。PowerShell 命令：

```powershell
Copy-Item -LiteralPath build/main.pdf -Destination main.pdf -Force
```

根目录 `main.pdf` 纳入版本控制；`build/` 中的日志、缓存、预览图及中间文件由 `.gitignore` 忽略。

## 内容维护

- 在 `chapter/` 中修改对应学科的 `.tex` 文件；新增、重排章节时同步维护 `main.tex` 和本页内容结构。
- 公式应注明定义域、参数范围、收敛与正则性条件；涉及等号、方向或符号约定时一并说明。
- 使用已有的章节标签进行交叉引用；补充文献时同步维护 `references.tex`。
- 提交前检查编译日志与新增页面，确认公式无越界、缺字及未解析引用，再更新根目录 PDF。
- 临时草稿、编译日志和预览图统一放入 `build/`，保留源文件、索引样式及正式图片资源。

## 许可

仓库采用 [MIT License](LICENSE)。参考文献及外部资料的出处见正文引用与 `references.tex`。
