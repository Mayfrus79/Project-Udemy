import os
import shutil

HOME = os.path.expanduser('~')

Caminho = os.path.join(HOME, 'Downloads', 'Bebeto')

shutil.rmtree(Caminho)