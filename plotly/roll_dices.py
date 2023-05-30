from plotly.graph_objs import Bar, Layout
from plotly import offline

from a_dice import Dice

dice_1 = Dice()
dice_2 = Dice()


# Моделирует броски трёх кубиков 1000 раз и сохраняет результаты.
results_rolls = [dice_1.roll_dice() + dice_2.roll_dice() for x in range(1000)]


max_result = dice_1.sides_dice + dice_2.sides_dice
# Считает частоту результатов из "results_rolls".
results_frequencies = [results_rolls.count(x) for x in range(2, max_result+1)]

# Визуализация результатов на графике.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=results_frequencies)]

x_axis_config = {'title': 'Результат', 'dtick': 1}
y_axis_config = {'title': 'Частота выпадения'}
layout = Layout(title='Результаты бросков двух шестигранных кубиков 1000 раз:',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': layout}, filename='d6_d6.html')
