import os
import matplotlib.pyplot as plt
import numpy as np

directory_path1 = './data/train/'
directory_path2 = './data/valid/'

dir_names = os.listdir(directory_path1)
file_count = [None] * len(dir_names)

i=0
for name in dir_names:
    dir = directory_path1+name
    file_count[i] = len(os.listdir(dir))
    i+=1
    
dir_names = os.listdir(directory_path2)

i=0

for name in dir_names:
    dir = directory_path2+name
    file_count[i] = file_count[i] + len(os.listdir(dir))
    i+=1

# --- Histogram ---

x = np.arange(len(dir_names))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, file_count, width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ilość')
ax.set_title('Histogram ilości zdjęć dla kodu znaku')
ax.set_xticks(x, dir_names,  rotation=90)

fig.tight_layout()

plt.show()
print('end')