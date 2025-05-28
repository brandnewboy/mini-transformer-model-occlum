import torch
from src.model import Model, enc  # 从model.py导入Model类和token编码器

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_full_model(model_path):
    """加载完整模型权重"""
    model = Model().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    return model

def load_split_model():
    """加载分块层权重"""
    model = Model().to(device)
    # 加载词嵌入层
    model.token_embedding_table.load_state_dict(torch.load("/data/token_embedding.pth", map_location=device))
    # 加载Transformer块
    for i, block in enumerate(model.transformer_blocks):
        block.load_state_dict(torch.load(f"/data/transformer_block_{i}.pth", map_location=device))
    # 加载最终线性层
    model.final_linear_layer.load_state_dict(torch.load("/data/final_linear.pth", map_location=device))
    return model

def evaluate_model(model, start='The'):
    """执行推理生成文本"""
    model.eval()
    start_ids = enc.encode(start)
    x = torch.tensor(start_ids, dtype=torch.long, device=device)[None, ...]  # 扩展batch维度
    y = model.generate(x, max_new_tokens=100)
    print('\n--------------------------------------------------------\n')
    print(enc.decode(y[0].tolist()))
    print('\n--------------------------------------------------------\n')

if __name__ == "__main__":
    # 选择加载模式：0为完整权重，1为分块权重
    model01 = load_full_model("/data/model.pth")
    model02 = load_split_model()
    
    evaluate_model(model01)
    evaluate_model(model02)