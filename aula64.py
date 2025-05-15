import os
import shutil

HOME = os.path.expanduser('~')
source_dir = os.path.join(HOME, 'Desktop', 'teste em python', 'Fichas')
destination_dir = os.path.join(HOME, 'Desktop', 'teste em python', 'Documentos fichas')

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

destination_dir = os.path.join(destination_dir, os.path.basename(source_dir))

print(HOME)

if not os.path.exists(destination_dir):
    shutil.copytree(source_dir, destination_dir)
    print(f'Folder successfully copied from {source_dir} to {destination_dir}')
else:
    print(f'Destination folder: {destination_dir} already exists, skipping copy.')

shutil.rmtree(os.path.join(HOME, 'Desktop', 'teste em python', 'Documentos fichas'))


