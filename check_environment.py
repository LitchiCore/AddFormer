"""学习第一步：确认当前 Python 环境和 GPU 是否可用。"""

import sys
import torch

# sys.executable 是运行当前文件的 Python 解释器路径。
print("Python 路径：", sys.executable)
print("PyTorch 版本：", torch.__version__)

# is_available() 会返回 True 或 False。
gpu_available = torch.cuda.is_available()
print("GPU 是否可用：", gpu_available)

# 只有 GPU 可用时，才查询第一张显卡的名称。
if gpu_available:
    print("显卡名称：", torch.cuda.get_device_name(0))
