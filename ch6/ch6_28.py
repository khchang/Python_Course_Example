# ch6_28.py
James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
games = len(James)                          # 求元素數量
score_Max = max(James[1:games])             # 最高得分
i = James.index(score_Max)                  # 場次
print(James[0], f"在第 {i} 場得最高分 {score_Max}")
    
