import os
directory_path = './data/train/'

dir_names = os.listdir(directory_path)
file_count = [None] * len(dir_names)

i=0
for name in dir_names:
    dir = directory_path+name
    file_count[i] = len(os.listdir(dir))
    i+=1

#test
for nums in file_count:
    print(nums)
