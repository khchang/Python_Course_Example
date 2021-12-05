# ch7_25.py
tuition = 50000
year = 0
while tuition < 60000:
    print(f"第 {year + 1} 年學費為 {tuition} 元")
    tuition = int(tuition * 1.05)
    year += 1
    
print(f"在第 {year + 1} 年後，學費為 {tuition} 元，會達到或超過60000元 ")

