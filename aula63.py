import math
import os
from itertools import count


def format_size(size_in_bytes: int, base: int = 1000) -> str:
    if size_in_bytes <= 0:
        return "0B"
    
    size_abbreviations = "B", "KB", "MB", "GB", "TB", "PB"
    abbreviation_index = int(math.log(size_in_bytes, base))
    power = base ** abbreviation_index
    final_size = size_in_bytes / power
    size_abbreviation = size_abbreviations[abbreviation_index]
    return f'{final_size:.2f} {size_abbreviation}'


path = os.path.join('/Users', 'larti', 'Downloads', 'Programas', 'teste')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Current folder:', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        full_file_path = os.path.join(root, file_)
        stats = os.stat(full_file_path)
        size = stats.st_size
        print('  ', the_counter, 'FILE:', file_, format_size(size))
