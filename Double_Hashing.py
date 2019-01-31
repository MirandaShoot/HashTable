class HashDoubleTable:
    def __init__(self):
        """Инициализируем таблицу с изначально заданним размером таблицы"""

        self.__size = 7
        self.__loadSize=7
        self.__сells = [None] * self.__size
        self.__value = [None] * self.__size
        self.__removed = "\0"
        self.__cnt = 0


    def getLength(self):
            """метод для проверки сколько заполненых элементов содержиться в таблице """
            length = self.__сells.__len__()
            return length


    def hash_function(self, key, size):
        """Первая хеш функция зависет от размера таблицы"""
        return key % size


    def rehash(self, old_hash, size):
        """Вторая хеш функция зависет от старого размера таблицы"""

        return size - (old_hash % (size - 1) + 1)

    def get(self, key):
        """Поиск по ключу , возвращает заданный ключ если он есть в противном случае возвращаем None"""

        start_slot = self.hash_function(key, len(self.__сells))
        position = start_slot
        while self.__сells[position] != None:
            if self.__сells[position] == key:
                return self.__value[position]
            else:
                position = self.rehash(position, len(self.__сells))
                if position == start_slot:
                    return None
        return None

    def put(self, key, data):
            """Вставка ключа и значения при этом ключ хешируем в ячейку таблицы """

            cnt=0
            hash_value = self.hash_function(key, len(self.__сells))

            if self.__сells[hash_value] == None or \
                    self.__сells[hash_value] == self.__removed:
                self.__сells[hash_value] = key
                self.__value[hash_value] = data
                self.__cnt += 1
                self.__len__()
                ns = self.__сells.__len__()
                if self.load() > 0.75:
                    self.resize(ns)
            elif self.__сells[hash_value] == key:
                self.__value[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.__сells))
                while self.__сells[next_slot] != None \
                        and self.__сells[next_slot] != self.__removed \
                        and self.__сells[next_slot] != key:
                    next_slot = self.rehash(hash_value, len(self.__сells))
                    cnt+=1
                    if(cnt>5):#устранения зацикливания
                        self.resize(self.__сells.__len__())
                    if next_slot == hash_value:
                        return
                if self.__сells[next_slot] == None or \
                        self.__сells[next_slot] == self.__removed:
                    self.__сells[next_slot] = key
                    self.__value[next_slot] = data
                    ns=self.__сells.__len__()
                    self.__cnt += 1
                    self.__len__()
                    if self.load() > 0.75:
                        self.resize(ns)
                else:

                    self.__value[next_slot] = data

    def delete(self, key):
        """Удаление  по ключу , удаляет заданный ключ если он есть в противном случае вовращем None"""

        start_slot = self.hash_function(key, len(self.__сells))
        position = start_slot
        key_in_slot = self.__сells[position]

        while key_in_slot != None:
            if key_in_slot == key:
                self.__сells[position] = self.__removed
                self.__value[position] = self.__removed
                self.__cnt -= 1
                self.__len__()
                return None
            else:
                position = self.rehash(position, len(self.__сells))
                key_in_slot = self.__сells[position]
                if position == start_slot:
                    return None
        return None

    def new_size(self, old_size):
        """Создаем новый размер таблицы при этом учитываем что размерм должен быть простым числом"""
        prime_list = []
        for i in range(old_size + 1, 2 * old_size + 1):
            if i == 2:
                prime_list.append(i)
            else:
                for j in range(2, i - 1):
                    if i % j != 0:
                        prime_list.append(i)

        if (self.isPrime(max(prime_list))):
            new_size = max(prime_list)
        else:
            num = max(prime_list)
            new_size = self.getPrimeNumber(num)
            self.__loadSize=new_size
        return new_size

    def isPrime(self,candidate):
        """Проверка простое ли число"""
        if (candidate % 2) == 0:
            if candidate == 2:
                return True
            else:
                return False
        for i in range(3, candidate, 2):
            if (i * i) > candidate:
                break;
            if (candidate % i) == 0:
                return False
        return candidate != 1

    def getPrimeNumber(self,n):
        """Получаем простое число"""
        while not self.isPrime(n):
            n += 1
        return n

    def resize(self,oldSize):
        """Перехешируем нашу таблицу в случае ее перезаполнености > 0.75"""
        new_size = self.new_size(oldSize)
        self.__cnt = 0
        new_slots = [None] * new_size
        new_data = [None] * new_size

        for key in self.__сells:
            if key != None:
                hash_value = key % new_size
                data = self.get(key)
                if new_slots[hash_value] == None:
                    new_slots[hash_value] = key
                    new_data[hash_value] = data
                    self.__cnt += 1
                    self.__len__()
                elif new_slots[hash_value] == key:
                     new_data[hash_value] = data
                else:
                    next_slot = self.rehash(hash_value, len(new_slots))
                    while new_slots[next_slot] != None \
                            and new_slots[next_slot] != key:
                        next_slot = self.rehash(next_slot, len(new_slots))
                        if next_slot == hash_value:
                            return
                    if new_slots[next_slot] == None:
                        new_slots[next_slot] = key
                        new_data[next_slot] = data
                        self.__cnt += 1
                        self.__len__()
                    else:
                        new_data[next_slot] = data
        self.__сells = new_slots
        self.__value = new_data
        self.__loadSize = new_size

    def __delitem__(self, key):
        return self.delete(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.__cnt

    def __contains__(self, key):
        return self.get(key) != None

    def load(self):
        """Фактор заполнености таблици"""
        return self.__cnt / self.__loadSize










