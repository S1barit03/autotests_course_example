# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('test_file/task_3.txt', 'r', encoding='utf-8') as purchases_file:
    raw_lst = []
    price = 0
    for i in purchases_file:
        if i != '\n':
            price+=int(i)
        else:
            raw_lst.append(price)
            price = 0
    raw_lst.sort()
    three_most_expensive_purchases = sum(raw_lst[-3:])

assert three_most_expensive_purchases == 202346
