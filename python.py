
import matplotlib.pyplot as plt
x = [3, 5, 2, 8, 7, 9, 3, 4, 6, 1]
y= []
for i in x:
    y.append(3*i+2)
# Box Plot
plt.boxplot(x)
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()

