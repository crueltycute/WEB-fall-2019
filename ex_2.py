from __future__ import print_function

from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']


def test_unique_iterator():
    print('TEST WITH LIST OF INTS')
    print(data1)
    for i in Unique(data1, ignore_case=False):
        print(i, end=' ')
    print('\n')

    print('TEST WITH GENERATOR OF INTS\ngen_random(1, 3, 10)')
    for i in Unique(data2, ignore_case=False):
        print(i, end=' ')
    print('\n')

    print('TEST WITH LIST OF STR (ignore_case=False)')
    print(data3)
    for i in Unique(data3, ignore_case=False):
        print(i, end=' ')
    print('\n')

    print('TEST WITH LIST OF STR (ignore_case=True)')
    print(data3)
    for i in Unique(data3, ignore_case=True):
        print(i, end=' ')


# Реализация задания 2
if __name__ == "__main__":
    test_unique_iterator()
