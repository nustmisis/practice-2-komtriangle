# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в  нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры. 
После того как все возможные номера были использованы, формат был 
изменен на четыре цифры, предшествующие трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак 
машины и оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите 
это в сообщении
"""

import re


def is_old_number(auto_number):
    return re.fullmatch(r'[А-Я]{3}[0-9]{3}', auto_number) is not None


def is_new_number(auto_number):
    return re.fullmatch(r'[0-9]{4}[А-Я]{3}', auto_number) is not None


auto_number = input()

if is_old_number(auto_number):
    print("Введённая последовательность - номер старого образца")
elif is_new_number(auto_number):
    print("Введённая последовательность - номер нового образца")
else:
    print("Введённая последовательность не соответсвую ни новому, ни старому формату авто номеров")
