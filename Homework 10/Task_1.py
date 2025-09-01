# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

def generate_random_name():
    while True:
        alph_lst = [chr(i) for i in range(97, 123)]
        #lst = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        length1 = random.randrange(1, 15)
        length2 = random.randrange(1, 15)
        word1, word2 = '', ''
        l, k = 1, 1
        while l <= length1:
            word1 += random.choice(alph_lst)
            l += 1
        while k <= length2:
            word2 += random.choice(alph_lst)
            k += 1
        l, k = 1, 1
        random_string = f"{word1} {word2}"
        yield random_string


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Здесь пишем код