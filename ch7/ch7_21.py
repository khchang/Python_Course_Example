# ch7_21.py
players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
for player in players:
    if player[1] < 200:
        continue            # continue, 不執行下面的指令，直接進下一個for-loop
    print(player)
    

