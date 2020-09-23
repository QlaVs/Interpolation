import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


class kursach:
    def __init__(self, n):
        self.sum = 0
        self.min = 1001
        self.max = -1001
        self.massive = []
        self.quantity = n
        self.writing = open('numbers.txt', 'w')
        self.reading = open('numbers.txt', 'r')

    def begin(self):
        with self.writing:
            for x in range(self.quantity):
                rand = random.uniform(-1000, 1000)
                self.writing.write(str(rand) + "\n")                          # заполнение txt #
        self.mass()

    def mass(self):
        with self.reading:
            for line in self.reading:
                for x in line.split():
                    self.massive.append(float(x))                            # создание массива #
        self.average()

    def average(self):
        self.sum = float(self.sum)
        for x in range(self.quantity):
            self.sum += self.massive[x]                                      # среднее значение #
        global result
        global summ
        summ = self.sum
        result = self.sum / self.quantity


# z = int(input('Кол-во чисел? : '))
z = 20
my_kursach = kursach(z)
my_kursach.begin()

numeric_massive = []

for p in range(my_kursach.quantity):
    numeric_massive.append(p)

numeric_massive = np.array(numeric_massive)
main_massive = np.array(my_kursach.massive)

'''
Создание "плавного" графика с использованием метода интерполяции
'''
x_smooth = np.linspace(numeric_massive.min(), numeric_massive.max(), 300)
spl = make_interp_spline(numeric_massive, main_massive)
y_smooth = spl(x_smooth)

'''
Задание сабплотов (подокон) для разделения рабочей области
'''
env, fig = plt.subplots(1, 2, figsize=(15, 5))

fig[1].axis('off')

fig[0].plot(x_smooth, y_smooth, label='Интерполир. график')
fig[0].plot(my_kursach.massive, label='Исходн. график')

frst_min = 1
frst_max = 1
x_ext = []
y_ext = []

'''
Нахождение и вывод макс и мин
'''
for i in range(1, len(y_smooth)-1):
    if (y_smooth[i - 1] < y_smooth[i]) and (y_smooth[i] > y_smooth[i + 1]):
        if frst_min == 1:
            fig[0].plot(x_smooth[i], y_smooth[i], 'ro', label='Max')
            x_ext.append(round(x_smooth[i], 3))
            y_ext.append(round(y_smooth[i], 3))
            frst_min = 0
        else:
            fig[0].plot(x_smooth[i], y_smooth[i], 'ro')
            x_ext.append(round(x_smooth[i], 3))
            y_ext.append(round(y_smooth[i], 3))

    elif (y_smooth[i - 1] > y_smooth[i]) and (y_smooth[i] < y_smooth[i + 1]):
        if frst_max == 1:
            fig[0].plot(x_smooth[i], y_smooth[i], 'go', label='Min')
            x_ext.append(round(x_smooth[i], 3))
            y_ext.append(round(y_smooth[i], 3))
            frst_max = 0
        else:
            fig[0].plot(x_smooth[i], y_smooth[i], 'go')
            x_ext.append(round(x_smooth[i], 3))
            y_ext.append(round(y_smooth[i], 3))

fig[0].plot(my_kursach.massive, '+', color='k')

r = str("%.3f" % result)
s = str("%.3f" % summ)
txt = [s, r]

'''
Вывод таблицы экстремумов
'''
fig[1].table(cellText=np.array([x_ext, y_ext]).transpose(), colLabels=("X координата экстремум", "Y координата экстремум"), loc='center', cellLoc='center')

'''
Вывод таблицы со средним значением и суммой всех чисел
'''
fig[1].table(cellText=np.array([txt]), colLabels=('Сумма чисел', 'Среднее значение'), loc='upper center', cellLoc='center')

'''
Вывод графика и легенды
'''
fig[0].legend(loc='lower left', bbox_to_anchor=(0.0, 1.01), ncol=2, borderaxespad=0, frameon=True)
fig[0].set_ylabel('Число')
fig[0].set_xlabel('Порядковый номер')
fig[0].set_xticks(range(z))


'''
Отображение на экране
'''
plt.show()
