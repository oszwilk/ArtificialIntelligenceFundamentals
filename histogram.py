import os
import matplotlib.pyplot as plt
import numpy as np

directory_path = './data/train/'

dir_names = os.listdir(directory_path)
file_count = [None] * len(dir_names)

i=0
for name in dir_names:
    dir = directory_path+name
    file_count[i] = len(os.listdir(dir))
    i+=1

# --- Histogram ---

x = np.arange(len(dir_names))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, file_count, width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ilość')
ax.set_title('Histogram')
ax.set_xticks(x, dir_names,  rotation=90)

fig.tight_layout()

plt.show()