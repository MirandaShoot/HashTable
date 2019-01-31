from linkedList import LinkedList


class HashTable(object):

    def __init__(self, init_size=12):
        """Инициализируем таблицу с начально заданным количеством списков"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Строковое представление хеш-таблицы, возвращает длинну """
        return 'HashTable({})'.format(self.length())

    def _hashFunc(self, key):
        """Хеш-функция которая возвращет индекс ячейки в которой будет записанно значение"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Возвращает длинну списка через его полный проход и подсчет узлов"""
        count = 0
        for bucket in self.buckets:
            # bucket should be a list containing the key value pairs
            count += bucket.length()
        return count

    def get(self, key):
        """Поиск по ключу , возвращает заданный ключ если он есть в противном случае вызываем KeyError"""
        bucket = self.buckets[self._hashFunc(key)]
        data = bucket.find(lambda node: node[0] == key)
        if data is not None:
            return data[1]

        raise KeyError

    def set(self, key, value):
        """Вставка ключа и значения при этом ключ хешируем в ячейку конкретного списка"""
        hashKey = hash(key) % len(self.buckets)
        bucket = self.buckets[hashKey]
        bucket.append((key, value))

    def delete(self, key):
        """Удаление  по ключу , удаляет заданный ключ если он есть в противном случае вызываем KeyError"""


        bucketIndex = hash(key) % len(self.buckets)
        bucket = self.buckets[bucketIndex]
        for node in bucket:
            if key == node.data[0]:
                bucket.delete(node.data)
                return
        raise KeyError


    def __iter__(self):
        """ Итерируем по элементам объекта."""
        for node in self.buckets:
            yield node



