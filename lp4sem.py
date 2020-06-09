import random
import matplotlib.pyplot as plt
import numpy as np

r = 6  # количество выстрелов
p = 0.8  # вероятность попадания
n = 100  # 1600 #100000 # число опытов
listOfX = [i for i in range(1, n + 1)]
listOfY = []


def P(countHit):
    count_good = 0  # число успехов (требуемое количество попаданий совпадает с текущим значением СВ)
    for i in range(0, n):  # n опытов
        count = 0  # число попаданий в опыте
        for j in range(0, r):  # r выстрелов
            attempt = random.randint(0, 100)
            if p * 100 >= attempt:
                count += 1
        if countHit == count:
            count_good += 1
    return count_good / n


def scatterplot(x_data, y_data, x_label="", y_label="", title="", color="r", yscale_log=False):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s=10, color=color, alpha=0.75)

    if yscale_log:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


random.seed(version=2)
for i in range(1, n+1):
    sumProbability = 0
    for j in range(1, r, 2):
        sumProbability += P(j)
    listOfY.append(sumProbability)

print(sumProbability)

# xt = np.linspace(-4, 4, 101)
# yt = 1/(xt**2+1)

# xe = np.linspace(1, 100, 21)
# yerr = 0.1 * np.ones(21)
# ye = 1/(xe**2 + 1) + yerr * np.random.normal(size=21)

print(len(listOfX))
print(len(listOfY))
scatterplot(listOfX, listOfY[0:n])
plt.show()
