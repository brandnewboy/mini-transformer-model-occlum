from transformers import AutoModel, AutoTokenizer


local_path = "/home/ystf/model_finger/model/huggingface/hub/models--THUDM--chatglm-6b"  # 本地模型路径
# 加载分词器
# tokenizer = AutoTokenizer.from_pretrained(local_path, trust_remote_code=True, use_fast=False)
# 加载模型
model = AutoModel.from_pretrained(local_path, trust_remote_code=True).half().cuda()
model = model.eval()

# 打印模型的基本信息
print("模型基本信息：")
print(model)

# 打印模型各层的详细信息
print("\n模型各层详细信息：")
for name, module in model.named_modules():
    print(f"层名称: {name}, 层类型: {type(module).__name__}")
