import csv 
import matplotlib.pyplot as plt 

x,y = [], []
with open('opendata.csv', 'r', encoding='utf-8') as file:
    r = csv.reader(file, delimiter=',')

    for row in r:
        if len(row) == 4:
            name = row[0]
            region = row[1]
            date = row[2]
            value = row[3]
        if '2018' in date and region == "Забайкальский край" and name == "Средняя пенсия":
            try:
                x.append(date)
                y.append(value)
            except (ValueError, TypeError):
                continue

full_value = sum([int(i) for i in y])/ len(y)
print(full_value)

plt.plot(x,y)
plt.xlabel("Дата")
plt.ylabel("Средняя пенсия")
plt.show()



