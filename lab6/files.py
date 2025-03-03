#1
import os

path = "."  # Текущая директория

# Только папки
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories:", directories)

# Только файлы
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files:", files)

# Все элементы
all_items = os.listdir(path)
print("All items:", all_items)
#2

def check_access(path):
    print("Existence:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# Пример использования
check_access('C:/Users')
#3

def check_path_info(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print('C:/Users/user/Desktop/example.txt')

# Пример использования
check_path_info('ttt.txt')
#4
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

# Пример использования
print(count_lines('lab6/ttt.txt'))
#5
def write_list_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(str(item) + '\n')

# Пример использования
write_list_to_file('output.txt', ['Hello', 'World', 123])
#6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")
#7
def copy_file(src, dest):
    with open(src, 'r', encoding='utf-8') as f1, open(dest, 'w', encoding='utf-8') as f2:
        f2.write(f1.read())

# Пример использования
copy_file('source.txt', 'destination.txt')
#8
import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"{path} deleted.")
    else:
        print("File does not exist or is not writable.")

# Пример использования
delete_file('example.txt')
