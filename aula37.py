# Define the file path
file_path = 'C:\\Users\\LarTi\\Desktop\\Novapastaprojeto\\'
file_path += 'aula116.txt'

# Open the file in write mode and write content to it
with open(file_path, 'w') as file:
    # Write content to the file
    file.write('Hello world\n')
    file.write('The file will be closed\n')
    file.write('Everything all right!\n')
    file.write('Atenção meu pau na sua mão!\n')
    
    
with open(file_path, 'a') as file:
    file.write('text appended to the end of the file.\n')

    # Print messages to the console
    print('Hello world')
    print('The file will be closed')
    print('Everything all right!')
    print('Atenção')
    print('text appended to the end of the file.')
    print()


