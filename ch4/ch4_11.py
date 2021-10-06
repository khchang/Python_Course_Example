# ch4_11.py
# 使用編號順序

score = 90
name = "張凱雄"
count = 1
# 以下鼓勵使用
print("{0}你的第 {1} 次物理考試成績是 {2}".format(name,count,score))
# {0}: name
# {1}: count
# {2}: score


# 以下語法對，但不鼓勵使用
print("{2}你的第 {1} 次物理考試成績是 {0}".format(score,count,name))
# {0}: score
# {1}: count
# {2}: name

