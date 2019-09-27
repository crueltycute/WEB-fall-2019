#!/usr/bin/env python3

from __future__ import print_function

from librip.gens import field
from librip.gens import gen_random


def test_gen_random():
    print('Rand begin:', end=' ')
    begin = int(input())

    print('Rand end:', end=' ')
    end = int(input())

    print('Rand num count:', end=' ')
    num_count = int(input())

    print('\n')

    print('gen_random() results:', end=' ')
    for i in gen_random(begin, end, num_count):
        print(i, end=' '),


def test_field_with_goods():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
        {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
    ]

    print(type(field(goods, 'title')))
    for i in field(goods, 'title', 'price'):
        print(i, end=' ')


# Реализация задания 1
def main():
    # test_gen_random()
    test_field_with_goods()


if __name__ == "__main__":
    main()
