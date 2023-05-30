import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
plt.grid()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=30)

plt.title('Square numbers', fontsize=18, c='#003366')
plt.ylabel('Square of value', fontsize=13, c='#990000')
plt.xlabel('Value', fontsize=13, c='#990000')

ax.tick_params(width=5, labelsize=10, color='#009900', direction='inout')
ax.axis([0, 110, 0, 12000])

plt.show()
