import pandas as pd
datos = pd.read_excel("OSS.xlsx")

# 1. The average bill
print(datos.Bill.mean())
print('*'*50)

# 2. average hours of delivery
print(datos.HoursUntilDelivery.mean())
print('*'*50)

# 3. top 5 states with the highest purchase volume (by number of orders)
print(datos.State.value_counts().head(5))
print('*'*50)

# 4. top 5 states with the highest order value
print(datos.groupby('State').Bill.sum().sort_values(ascending=False).head(5))
print('*'*50)

# 5. 21st-25th cities when sorted by number of orders
print(datos.State.value_counts(ascending=True).head(25).tail(5))
print('')

print(datos.groupby('State').OrderID.count().sort_values(ascending=True).head(25).tail(5))
print('*'*50)

# 6. amount of orders for each year
print(datos.OrderYear.value_counts().sort_index())
print('*'*50)

# 7. total spending by customer, top 3
print(datos.groupby('CustomerName').Bill.sum().sort_values(ascending=False).head(3))
print('*'*50)

# 8. the earliest and the lastest order day
print(datos.OrderDate.min())
print(datos.OrderDate.max())
print('*'*50)

# 9. the most expensive bill in each segment
print(datos.groupby('Segment').Bill.max())
print('*'*50)

# 10. average delivery time by customer name
print(datos.groupby('CustomerName').HoursUntilDelivery.mean().tail(5))
print('*'*50)

# 11. month week
datos["OrderDate"] = pd.to_datetime(datos["OrderDate"])
datos["Month"] = datos.OrderDate.dt.month
datos["Weekday"] = datos.OrderDate.dt.day_name()

# 每月订单量 / 收入
print(datos.groupby("Month").Bill.agg(["count", "sum"]))
print('*'*50)

# 哪个月最忙
print(datos.Month.value_counts().head(3))
print('*'*50)

# 星期几下单最多
print(datos.Weekday.value_counts())
print('*'*50)