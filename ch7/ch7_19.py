# ch7_19.py
print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break                   # 遇break強制離開for-loop
    print(digit, end=', ')
print()


print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break                   # 遇不到break
    print(digit, end=', ')


