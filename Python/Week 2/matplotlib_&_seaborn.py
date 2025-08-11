# Data--------------------------------------------
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


import matplotlib.pyplot as plt

"""
Create a figure object called `fig` using `plt.figure()`.
Use `add_axes` to add an axis to the figure canvas at [0,0,1,1]. Call this new axis `ax`.
Plot (x,y) on that axes and set the labels and titles to match the plot below:
"""
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


"""**Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**"""
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])


"""**Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**"""
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax1.plot(x,z)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])


"""**Use plt.subplots(nrows=1, ncols=2) to create the plot below.**"""
fig = plt.figure()
ax1 = fig.add_axes([0,0,0.35,0.8])
ax2 = fig.add_axes([0.43,0,0.35,0.8])


"""**Now plot (x,y) and (x,z) on the axes.**"""
fig = plt.figure()
ax1 = fig.add_axes([0,0,0.35,0.8])
ax2 = fig.add_axes([0.45,0,0.35,0.8])

ax1.plot(x, y, color='blue', linestyle='dashed', linewidth=3, markersize=12)
ax2.plot(x,z, color='red', linewidth=3.5)

# SEABORN--------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

# code here to load the dataset as a dataframe from seaborn datasets
data = sns.load_dataset('penguins')
data.info()

# data['species'].unique()
sns.barplot(x='species', y='flipper_length_mm', data=data, hue='species')
plt.title('Flipper Length for Penguin Species')


sns.violinplot(x='species', y='flipper_length_mm', data=data, hue='species')
plt.title('Flipper Length for Penguin Species')


sns.pairplot(data, hue='species')


correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='rocket_r')


sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', data=data, hue='species')
plt.title('Bill Length vs Bill Depth')