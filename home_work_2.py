from pandas import DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})
data.head()

# Создаю случайные данные
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})

# Создаю новые столбцы для каждого уникального значения
for value in data['whoAmI'].unique():
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляю столбец whoAmI
data.drop('whoAmI', axis=1, inplace=True)

# Вывод результата
print(data.head())