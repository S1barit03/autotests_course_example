# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

from pathlib import Path

with open('test_file/task1_answer.txt', 'a+', encoding='utf-8') as new_file:
    with open('test_file/task1_data.txt', 'r', encoding='utf-8') as old_file:
        new_line = ''
        new_lst = []
        for old_line in old_file.readlines():
            for letter in old_line:
                if letter not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n']:
                    new_line = new_line + letter
            new_lst.append(new_line)
            new_line = ''
        new_text = '\n'.join(new_lst)
        new_file.writelines(new_text)



# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
