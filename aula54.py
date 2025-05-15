class Myopen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Abrir arquivo aqui -->')
        self._file = open(self.file_path, self.mode, encoding = 'UTF8')
        return self._file
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('fechando o arquivo aqui')
        self._file.close()

with Myopen('Teste de criação.txt', 'w') as file:
    file.write('teste linha 1\n')
    file.write('teste linha 2\n')
    file.write('teste linha 3\n')
    print('WITH vem aqui', file)