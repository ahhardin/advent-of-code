import requests
import re

from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/7/input', headers={'Cookie': SESSION})
today_data = response.content.decode('utf-8').strip().split('\n')

test_data = [
  "$ cd /",
  "$ ls",
  "dir a",
  "14848514 b.txt",
  "8504156 c.dat",
  "dir d",
  "$ cd a",
  "$ ls",
  "dir e",
  "29116 f",
  "2557 g",
  "62596 h.lst",
  "$ cd e",
  "$ ls",
  "584 i",
  "$ cd ..",
  "$ cd ..",
  "$ cd d",
  "$ ls",
  "4060174 j",
  "8033020 d.log",
  "5626152 d.ext",
  "7214296 k",
]

PATTERNS = dict(
    move_pattern="\$ cd ([\w/.]+)",
    list_pattern="\$ ls",
    dir_pattern="dir (\w+)",
    file_pattern="(\d+) ([\w.]+)",
)

class Dir:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.subdirs = []
        self.files = []
    
    @property
    def child_mapping(self):
        return {c.name: c for c in self.subdirs + self.files}
    
    @property    
    def size(self):
        return sum(item.size for item in self.files + self.subdirs)
    
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

def get_top(directory):
    if not directory.parent:
        return directory
    return get_top(directory.parent)

def execute_line(directory, line):
    instruction = next(
        (key, re.search(val, line)) for key, val in PATTERNS.items() if re.search(val, line) is not None
    )
    # move
    if instruction[0] == "move_pattern":
        loc = instruction[1].groups()[0]
        if loc == "..":
            return directory.parent or get_top(directory)
        elif loc == "/":
            return get_top(directory)
        else:
            # go to loc if exists
            if loc in directory.child_mapping.keys():
                return directory.child_mapping[loc]
            # else create loc and then go there
            else:
                subdir = Dir(loc, directory)
                directory.subdirs.append(subdir)
                return subdir
    # create subdir
    if instruction[0] == "dir_pattern":
        name = instruction[1].groups()[0]
        if name in directory.child_mapping.keys():
            return directory
        subdir = Dir(name, directory)
        directory.subdirs.append(subdir)
        return directory
    # create file
    if instruction[0] == "file_pattern":
        name = instruction[1].groups()[1]
        size = instruction[1].groups()[0]
        if name in directory.child_mapping.keys():
            return directory
        file = File(name, size)
        directory.files.append(file)
        return directory
    return directory
    
def build_directory(instructions):
    directory = Dir("top", None)
    for item in instructions:
        directory = execute_line(directory, item)
    return get_top(directory)
        
test = build_directory(test_data)

assert(test.size == 48381165)

SIZE_LIMIT = 100000

def find_dirs_less_than_size(directory, sizes=None):
    sizes = sizes or []
    for subdir in directory.subdirs:
        if subdir.size <= SIZE_LIMIT:
            sizes.append(subdir.size)
        if subdir.subdirs:
            sizes = find_dirs_less_than_size(subdir, sizes)
    return sizes

test_sizes = find_dirs_less_than_size(test)
assert(sum(test_sizes) == 95437)

part_1_dir = build_directory(today_data)
part_1_sizes = find_dirs_less_than_size(part_1_dir)
print(f"part 1: {sum(part_1_sizes)}")

MAX_SIZE = 70000000
SIZE_NEEDED = 30000000

def find_dirs_greater_than_size(directory, size_min, sizes=None):
    sizes = sizes or []
    for subdir in directory.subdirs:
        if subdir.size >= size_min:
            sizes.append(subdir.size)
        if subdir.subdirs:
            sizes = find_dirs_greater_than_size(subdir, size_min, sizes)
    return sizes

def directory_to_delete(directory):
    min_size_to_delete = SIZE_NEEDED - (MAX_SIZE - directory.size)
    return min(find_dirs_greater_than_size(directory, min_size_to_delete))

assert(directory_to_delete(test) == 24933642)

print(f"part 2: {directory_to_delete(part_1_dir)}")
