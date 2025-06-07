# 🚀 (occlum LibOS)TEE_Model_privacy
## 项目简介
本项目利用蚂蚁集团的 Occlum（TEE LibOS 快速开发框架）对自行编写的 Mini 版 Transformer 模型进行隐私保护。
借助这个案例，你能快速体验 TEE 与大模型隐私保护的完美结合，深入探索在实际场景中保障模型隐私与安全的奥秘。

`*！！！文档还不完善，后期更新！！！*`

## 项目结构
```plaintext
.
├── .git/                   # Git 版本控制目录 🗂️
├── .idea/                  # IDE 配置目录 🛠️
├── build_occlum_instance.sh # 构建 Occlum 实例的脚本 🚧
├── config.yaml             # Occlum 配置文件 ⚙️
├── data/                   # 数据目录 📂
│   ├── cl100k_base.tiktoken # 编码配置文件 📄
│   ├── final_linear.pth    # 最终线性层权重文件 💾
│   ├── model.pth           # 完整模型权重文件 💾
│   ├── sales_textbook.txt  # 训练数据文件 📖
│   ├── token_embedding.pth # 词嵌入层权重文件 💾
│   └── transformer_block_*.pth # Transformer 块权重文件 💾
├── demo.py                 # 模型演示脚本 🎭
├── install_deps_with_conda.sh # 使用 Conda 安装依赖的脚本 📦
├── main.py                 # 主程序入口 🚪
├── run_python_on_occlum.sh # 在 Occlum 中运行 Python 程序的脚本 🐍
├── src/                    # 源代码目录 🧑‍💻
│   └── model.py            # Mini Transformer 模型定义文件 🧠
└── test.py                 # 测试脚本 🧪
```

## 环境准备
### 安装依赖
运行以下脚本使用 Conda 安装所需的 Python 环境和依赖：
```bash
./install_deps_with_conda.sh
```
📦 此操作将快速搭建项目所需的依赖环境，为后续运行保驾护航。


### 构建 Occlum 实例
执行以下脚本构建 Occlum 实例：
```bash
./build_occlum_instance.sh
```
🚧 成功构建 Occlum 实例，为模型隐私保护提供安全的运行环境。

## 模型相关
### 模型定义
Mini Transformer 模型定义在 src/model.py 文件中，包含词嵌入层、多个 Transformer 块和最终线性层。🧠

### 模型保存
src/model.py 中的 save_model 函数可将模型各层的权重分别保存到 data 目录下：
```python
def save_model(model):
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # 保存词嵌入层权重
    torch.save(model.token_embedding_table.state_dict(), "data/token_embedding.pth")
    
    # 保存 Transformer 块权重
    for i, block in enumerate(model.transformer_blocks):
        torch.save(block.state_dict(), f"data/transformer_block_{i}.pth")
    
    # 保存最终线性层权重
    torch.save(model.final_linear_layer.state_dict(), "data/final_linear.pth")
```
💾 通过分块保存，方便对模型各层进行管理和操作。

## 模型加载
main.py 中提供了两种模型加载方式：完整权重加载和分块权重加载：
```python
D:\Work\cqupt\大模型隐私保护\TEE_occlum\mini_transformer_model\main.py
Apply
if __name__ == "__main__":
    # 选择加载模式：0 为完整权重，1 为分块权重
    model01 = load_full_model(public_path + "/model.pth")
    model02 = load_split_model()
    
    evaluate_model(model01)
    evaluate_model(model02)
```
🔄 灵活的加载方式，满足不同场景的需求。

## 运行项目
在 Occlum 中运行 Python 程序：
```bash
./run_python_on_occlum.sh
```
🐍 一键启动，让模型在安全的环境中运行起来。


## 注意事项
确保网络连接正常，部分脚本需要从网络下载依赖和数据。📡
若使用 GPU 加速，请确保 CUDA 环境配置正确。🖥️


## 未来计划
- occlum 环境配置目前存在较大问题，后期完善，尽量实现更便捷的配置
- TEE应用与外界通信功能，`grpc` / `http-server` / `shared-FS`
- 文档完善......

