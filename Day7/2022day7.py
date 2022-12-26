import os, re, time

async def make_tree(tree_txt):
    """ Turns a CLI read-out into an actual directory within the current working directory """
    for i, line in enumerate(tree_txt):
        cur_dir = os.getcwd()
        if i == 0:
            os.mkdir(os.path.join(cur_dir,'ROOT'))
            os.chdir('ROOT')
        elif '$ cd' in line:
            os.chdir(line.replace('$ cd ',''))
        elif 'dir' in line:
            new_dir = line.replace('dir ','')
            new_path = os.path.join(cur_dir, new_dir)
            os.mkdir(new_path)
        elif '$ ls' in line:
            pass
        else:
            os.mkfifo(line)
    return

async def find_sizes():
    """ Goes through ROOT directory to find the total size of each directory within ROOT """
    dirpaths = []
    flat_sizes = []
    for path, dirs, files in os.walk('ROOT', topdown=True):
        dirpaths.append(path)
        total = 0 
        for f in files:
            file_size_list = re.findall('\d+',f)
            file_size = [int(x) for x in file_size_list]
            total += sum(file_size)
        flat_sizes.append(total)
    full_sizes = flat_sizes.copy()
    for i, path1 in enumerate(dirpaths):
        for j, path2 in enumerate(dirpaths):
            if (path1 in path2) and (path1 is not path2):
                full_sizes[i] += flat_sizes[j]
    return full_sizes
                    
#PART I 
#Find all of the directories with a total size of at most 100000 
#What is the sum of the total sizes of those directories?

#PART II
#The total disk space available to the filesystem is 70000000. 
#To run the update, you need unused space of at least 30000000. 
#You need to find a directory you can delete that will free up enough space to run the update.

#Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
#What is the total size of that directory?

with open('example_input.txt') as f:
    data_txt = f.readlines()
tree_txt = [line.strip() for line in data_txt]

""" FOR SOME REASON THIS CODE WILL ONLY WORK IF I RUN ONE OF THESE AT A TIME
- I HAVE TO RUN make_tree AND THEN START THE PROGRAM OVER TO RUN full_sizes AND MOVE ON
I HAVE TRIED time.wait() AND IT DOES NOT WORK"""
make_tree(tree_txt)
full_sizes = find_sizes()

unused_space = 70000000 - full_sizes[0]
to_free = 30000000 - unused_space

sum_sizes = 0
big_enough = []
for dir_size in full_sizes:
    if dir_size <= 100000:
        sum_sizes += dir_size
    if dir_size >= to_free:
        big_enough.append(dir_size)
big_enough.sort()    

print('The sum of the total sizes of all directories of at most 100000 is',sum_sizes)
print('The total size of the smallest directory we could delete is',big_enough[0])
