# AddFormer

一个不知是何意味的Transformer加法器

从零学习分词器、Transformer 和训练流程，第一阶段只做非负整数加法。

## 目录结构

```text
AddFormer/
├── addformer/           # 核心代码：分词器、数据生成、模型、训练和推理
├── configs/             # 模型和训练配置
├── scripts/             # 辅助脚本，例如数据导出
├── tests/               # 检查分词和加法数据等行为
├── docs/                # 学习笔记和实验说明
├── data/                # 生成的训练、验证和测试数据（不提交 Git）
├── checkpoints/         # 保存的模型权重（不提交 Git）
├── runs/                # 每次训练的日志（不提交 Git）
├── outputs/             # 图表、评估报告和预测结果（不提交 Git）
├── .venv/               # 项目独立 Python 环境（不提交 Git）
└── check_environment.py # 环境检查入口
```

后续分词器写在 `addformer/tokenizer.py`。目录先准备好，代码随学习进度逐步补充。
Git 不记录空目录，因此尚无文件的代码和文档目录用 `.gitkeep` 占位；生成产物目录只保留在本地。

## 本地环境

当前环境：Windows、Python 3.12、NVIDIA GPU。依赖安装在项目自己的 `.venv` 中。

已在 Python 3.12.10、PyTorch 2.11.0+cu128、RTX 4070 SUPER 上验证 GPU 前向计算、反向传播、AdamW 参数更新和 BPE 编码/解码。PyTorch 文件复用了本机兼容环境，重新安装到本项目后验证通过。

在项目目录使用 PowerShell 创建或恢复环境：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.lock.txt
```

`requirements.lock.txt` 固定了当前验证过的依赖版本，并指定 PyTorch 的 CUDA 12.8 软件源，适用于当前 Windows GPU 环境。`pyproject.toml` 记录直接依赖。

可以直接使用环境里的 Python，不必激活环境或修改 PowerShell 执行策略：

```powershell
.\.venv\Scripts\python.exe -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

也可以在当前终端激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

`.venv`、生成的数据和训练权重不提交到 Git。
