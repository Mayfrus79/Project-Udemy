from pathlib import Path
from shutil import rmtree

desktop = Path.home() / "Desktop" / "my_folder"
desktop.mkdir(exist_ok=True)

subfolder = desktop / "my_subfolder"
subfolder.mkdir(exist_ok=True)

text_file = subfolder / "my_file.txt"
with open(text_file, 'w', encoding='utf-8') as file:
    file.write("I'm learning to work with files in Python!\n\n")
    file.write("I can write multiple lines:\n")
    file.write("- Line 1\n")
    file.write("- Line 2\n")
 
print(f'The file was successfully created at: {text_file}')

files = subfolder / 'files'
files.mkdir(exist_ok=True)

for i in range(11): 
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()
        
    with open(file, 'w', encoding='utf-8') as file_order:
        file_order.write('Hello world\n')
        file_order.write(f'file_{i}.txt')

print(f"Files were successfully created in the 'files' folder.")

rmtree(desktop)
if not desktop.exists():
    print('All the files were erased! Have a good day!')

