import re
from utils import read_data


class FileSystemNode(object):
    def __init__(self, name='root', size=None):
        self.name = name
        self.parent = None
        self.size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_size(self):
        return self.size or sum(filter(None, [child.get_size() for child in self.children]))


data = read_data(7)
current_node = root = FileSystemNode("/")
# I could do the tree traversal, but I'm not at a job interview
all_directories = [root]

for line in data:
    if line == "$ ls":
        continue
    if line == "$ cd ..":
        current_node = current_node.parent
        continue
    if line == "$ cd /":
        current_node = root
        continue
    if new_current_directory_name := re.search(r'\$ cd ([a-z]+)', line):
        current_node = next((x for x in current_node.children 
                             if x.name == new_current_directory_name.group(1)), None)
        continue
    if new_child_directory_name := re.search(r'dir ([a-z]+)', line):
        new_child_directory = FileSystemNode(new_child_directory_name.group(1))
        all_directories.append(new_child_directory)
        current_node.add_child(new_child_directory)
        continue
    if file_description := re.search(r'([0-9]+) ([a-z\.]+)', line):
        current_node.add_child(FileSystemNode(name=file_description.group(2), 
                                              size=int(file_description.group(1))))
        continue
    raise ValueError(f"String pattern '{line}' cannot be recognized")

print(sum([node.get_size() for node in all_directories
           if node.get_size() <= 100000]))

space_to_clear = 30000000 - (70000000 - root.get_size())
print(min([node.get_size() for node in all_directories
           if node.get_size() >= space_to_clear]))
