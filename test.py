# 获取时间戳并计算某段程序运行时间
import time
start_time = time.time()
# 程序
end_time = time.time()
print(f"程序运行时间：{end_time - start_time}秒")
# 推理： inference.py