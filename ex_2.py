#!/usr/bin/env python3
from __future__ import print_function

from librip.gens import gen_random
from librip.iterators import Unique


# data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']


# Реализация задания 2
def main():
    try:
        for i in Unique(data3, ignore_case=True):
            print(i, end=' ')
    except IndexError:
        pass


if __name__ == "__main__":
    main()
