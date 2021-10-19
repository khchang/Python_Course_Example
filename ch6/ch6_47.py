# ch6_47.py
x = 10
y = 10
z = 15
r = 20
print(f"x = {x}, y = {y}, z = {z}, r = {r}")
print(f"x位址 = {hex(id(x))}, y位址 = {hex(id(y))}, z位址 = {hex(id(z))}, r位址 = {hex(id(r))}")
     
r = x                               # r的值將變為10
print(f"x = {x}, y = {y}, z = {z}, r = {r}")
print(f"x位址 = {hex(id(x))}, y位址 = {hex(id(y))}, z位址 = {hex(id(z))}, r位址 = {hex(id(r))}")
      



