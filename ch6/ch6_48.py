# ch6_48.py
x = 10
y = 10
z = 15
r = z - 5

boolean_value = x is y
print("is運算式")
print(f"x位址 = {hex(id(x))}")
print(f"y位址 = {hex(id(y))}")
print(f"x = {x}, y = {y}, ", boolean_value)

print("========== 我是分隔線 ==========")

boolean_value = x is z
print("is運算式")
print(f"x位址 = {hex(id(x))}")
print(f"z位址 = {hex(id(z))}")
print(f"x = {x}, z = {z}, ", boolean_value)

print("========== 我是分隔線 ==========")

boolean_value = x is r
print("is運算式")
print(f"x位址 = {hex(id(x))}")
print(f"r位址 = {hex(id(r))}")
print(f"x = {x}, r = {r}, ", boolean_value)

print("========== 我是分隔線 ==========")

boolean_value = x is not y
print("is not運算式")
print(f"x位址 = {hex(id(x))}")
print(f"y位址 = {hex(id(y))}")
print(f"x = {x}, y = {y}, ", boolean_value)

print("========== 我是分隔線 ==========")

boolean_value = x is not z
print("is not運算式")
print(f"x位址 = {hex(id(x))}")
print(f"z位址 = {hex(id(z))}")
print(f"x = {x}, z = {z}, ", boolean_value)

print("========== 我是分隔線 ==========")

boolean_value = x is not r
print("is not運算式")
print(f"x位址 = {hex(id(x))}")
print(f"r位址 = {hex(id(r))}")
print(f"x = {x}, r = {r}, ", boolean_value)


