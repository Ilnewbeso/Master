import pandas as pd

# pd.read_excel
# pd.read_csv

# datos = pd.read_excel("AVE.xlsx")

datos = pd.read_clipboard()
# print(datos)


print(datos.shape) # 看多少行 多少列
print('')
print(datos.columns) # 列名
print('')
print(datos.info()) # 看表信息
print('')
print(datos.head(3)) # 看表前几行数据
print('')
print(datos.tail(2)) # 看表最后几行数据
print('')

# frequencies in a column
# amount of times for each destiny
print(datos.destination.value_counts())
print('')

# amount of times for each destiny considering
# only the first 10 tickets
print(datos.head(10).destination.value_counts())
print('')

# same analysis for only the row 10, 11, 12, 13
print(datos.head(15).tail(4).destination.value_counts())

# average ticket price 
print(datos.price.mean())
print('')

# the most expensive price
print(datos.price.max())
print('')

# the total income for renfe
print(datos.price.sum())

# 3 most expensive tickets
top3 = datos.sort_values(by="price", ascending=True).tail(3)
print(top3.destination)
print(top3)

# avg price by train_type
print(datos.groupby(by="train_type").price.mean())

# total income for renfe by destination
print(datos.groupby(by="destination").price.sum())

# tickets by destination for each type of fare
datos.fare.unique()

from plotnine import *
for i in datos.fare.unique():
    aux = datos.loc[datos.fare == i,:]
    a = ggplot(aes(x="destination"), aux) + geom_bar(fill='red')
    a.save('Tickets by destination for' + i + '.pdf')