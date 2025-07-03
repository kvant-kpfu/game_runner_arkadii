import os



def recreate_file(fileName):
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write('"when Im gone".\n')
        f.write('makes me cry every time I hear it.\n')


def walk_dir(path):
    for root, dirs, files in os.walk(path):
        print(f'\nCurrent dir: {root}')
        print('Поддиректории:', dirs)
        print('Файлы:', files)