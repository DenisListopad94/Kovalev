import regex as re

# Вам дана строка.
# Выведите все подстроки, содержащие "cat".
input_string = input() #для удобства в некоторых задачах далее использовался этот ввод
print(*re.findall(r'\b\w*cat\w*\b', input_string))

# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
print(*re.findall(r'\bz\w{3}z\w*\b', input_string))

# Номер должен быть длиной 10 знаков и начинаться с 8 или 9.
# Есть список телефонных номеров, и нужно проверить их, 
# используя регулярные выражения в Python

numbers = []
while True:
    temp = input()
    if temp == 'Enough':
       break
    numbers.append(temp)
for number in numbers:
    if re.fullmatch(r'[89]\d{9}', number):
        print(f'Number {number} valid')
    else:
        print(f'Number {number} not valid')

# Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
print(*re.findall(r'\b[aeuio]\w*\b', input_string))

# Дана строка. Вывести все числа этой строки, как отрицательные так и положительные. 
print(re.findall(r'(?<=^|\s)-?\d+\b', input_string))

# В каждой строке замените все вхождения подстроки "human" 
# на подстроку "computer" и выведите полученные строки.
list_of_strings = []
while True:
    string = input()
    if string == '.':
       break
    list_of_strings.append(string)
result = []
i = 0
for string in list_of_strings:
    result.append(re.sub(r'human', r'computer', string))
    print(result[i])
    i += 1

# Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).
print(*re.findall(r'\b\d{2}-\d{2}-\d{4}\b', input_string))

# Найти все слова, в которых есть хотя бы одна буква ‘b’
print(*re.findall(r'\b\w*b+\w*\b', input_string))

# В каждой строке замените все вхождения нескольких 
# одинаковых букв на одну букву. Буквой считается символ из группы \w. 
list_of_strings = []
while True:
    string = input()
    if string == '.':
       break
    list_of_strings.append(string)
result = []
i = 0
for string in list_of_strings:
    result.append(re.sub(r'(\w)\1{2,}', r'\1', string))
    print(result[i])
    i += 1

# Поиск URL. Это регулярное выражение находит URL-адреса, 
# начинающиеся с "http://" или "https://", далее допускается 
# "www." (опционально), за которым следует доменное имя, а
# затем дополнительный путь и параметры.
print(*re.findall(r'http[s]?://[www.]?.+[.]{1}\w+\b', input_string))

# Напишите регулярное выражение для поиска всех HTML тегов в тексте
print(*re.findall(r'<[^>]+>',input_string))