# ch2_2.py (加上註解)
hourly_salary = 125                             # 設定時薪 (時薪 = 125)
annual_salary = hourly_salary * 8 * 300         # 計算年薪 (年薪 = 時薪 * 每日工時 * 每年工作日)
monthly_fee = 9000                              # 設定每月花費 (每月花費 = 9000)
annual_fee = monthly_fee * 12                   # 計算每年花費 (每年花費 = 每月花費 * 12個月)
annual_savings = annual_salary - annual_fee     # 計算每年儲存金額 (每年可存下的錢 = 年薪 - 每年花費)
print(annual_savings)                           # 列出每年儲存金額
