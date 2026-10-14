# 词表：模型允许使用的全部符号。
tokens = ["<PAD>", "<BOS>", "<EOS>"] + list("0123456789+=")
# <BOS>	Begin Of Sequence，序列开始	标记一条样本开始
# <EOS>	End Of Sequence，序列结束	模型生成它后，就停止回答
# <PAD>	Padding，填充	把同一批里的不同长度样本补到一样长

# 字典：保存“符号 → 编号”的对应关系。
token_to_id = {}

for index, token in enumerate(tokens):
    # enumerate(tokens) ：每次提供两个东西：位置编号和该位置的元素。Python 分别把它们赋给 index 和 token
    token_to_id[token] = index


# 编码部分
def encode(text):
    ids = []

    for character in text:
        token_id = token_to_id[character]
        ids.append(token_id)

    return ids
    # return ids：把算好的列表交给调用它的地方。


# 解码部分
def decode(ids):
    text = ""

    for token_id in ids:
            character = tokens[token_id]
            text += character

    return text

sample_text = "12+3=15"

bos_id = token_to_id["<BOS>"]
eos_id = token_to_id["<EOS>"]

sample_ids = [bos_id] + encode(sample_text) + [eos_id]

print("样本编号：", sample_ids)
print("样本内容：", decode(sample_ids))