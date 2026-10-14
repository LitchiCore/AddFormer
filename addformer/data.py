import csv
import random
from pathlib import Path


def make_example(a, b):
    result = a + b
    text = f"{a}+{b}={result}"
    return text


# 找到项目根目录，再确定保存位置。
project_dir = Path(__file__).resolve().parent.parent
# __file__ ：Python 提供的变量，表示当前文件的路径。
# Path(__file__) ：把路径转换成 Path 对象，方便操作文件和目录。
# .resolve() ：得到解析后的绝对路径。D:\LitchiCore\LitchiLab\AddFormer\addformer\data.py
file_path = project_dir / "data" / "examples.csv"

# 写cvs
with open(file_path, "w", encoding="utf-8", newline="") as file:
# with ：进入一段需要使用资源的代码，并在结束时自动收尾。
# open(...) ：打开文件。
# "w" ：写入模式（write），文件不存在创建文件。文件已经存在清空原内容再重新写入。
# newline="" ：让 Python 的文件层不转换换行符
    writer = csv.writer(file)
    # 创建一个 CSV 写入工具，告诉它把内容写到 file 这个文件中，然后用变量 writer 保存这个工具。
    writer.writerow(["a", "b", "result", "text"])
    # writerow() ：把这些数据写成一行。

    for index in range(100):
    # range(100)：提供 0～99，让循环执行 100 次。
        a = random.randint(0, 999)
        b = random.randint(0, 999)
        text = make_example(a, b)

        writer.writerow([a, b, a + b, text])

print("数据已保存到：", file_path)
