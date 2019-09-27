# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.limit = len(items)

        self.current = 0

        self.ignore_case = kwargs.get('ignore_case')

        if self.ignore_case:
            self.unique_dict = dict()
        else:
            self.unique = set()
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        if self.ignore_case:
            if self.items[self.current].lower() in self.unique_dict:
                while self.items[self.current].lower() in self.unique_dict:
                    self.current += 1
                    if self.current + 1 > self.limit:
                        break

            self.unique_dict.update({self.items[self.current].lower(): self.items[self.current]})
            return self.items[self.current]
        else:
            if self.items[self.current] in self.unique:
                while self.items[self.current] in self.unique:
                    self.current += 1
                    if self.current + 1 > self.limit:
                        break

            self.unique.add(self.items[self.current])
            return self.items[self.current]

    def __iter__(self):
        return self
