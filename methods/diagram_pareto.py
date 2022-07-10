
"""""

С помощью этого метода вы можете определить проблемные зоны и пошагово найти решение.

Диаграмма Парето может быть:

По результатам деятельности (выявляет главные проблемы).
По причинам (выявляет основные причины).
Построение диаграммы складывается из 7 этапов:

    Определение проблемы.
    Создание списка причин, которые провоцируют проблему.
    Подсчет количества возникновений каждой причины за определенный промежуток времени.
    Составление таблицы с данными, которые расположены в порядке убывания по значимости.
    Отображение данных в системе координат. Ось абсцисс — перечень факторов, ось ординат — 
    величина вклада факторов в решение проблемы.
    Создание диаграммы по каждой отдельной причине проблемы.  Высота столбиков должна уменьшаться слева направо.
    Анализ результатов по диаграмме.

"""""
import matplotlib.pyplot as plt
import numpy as np

class MethodDiagramPareto():
    def __init__(self):
        ...

    def get_problem(self):
        problem = input("Введите проблему: ")
        return  problem

    def get_causes(self):
        causes = input("Введите причины через запятую: ").split(",")
        freq_causes = input("Введите частоту каждой причины через запятую:").split(",")
        count_causes = len(causes)
        return causes, count_causes, freq_causes

    def get_diagram(self):
        problem = MethodDiagramPareto().get_problem()
        causes, count_causes, freq_causes = MethodDiagramPareto().get_causes()

        width = 0.35
        fig, ax = plt.subplots()
        ax[0].bar(causes, freq_causes)
        plt.show()

    def display(self):
        p = MethodDiagramPareto().get_problem()
        c = MethodDiagramPareto().get_causes()
        d = MethodDiagramPareto().get_diagram()




test1 = MethodDiagramPareto().display()



