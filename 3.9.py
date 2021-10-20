class Vector:

    def __init__(self, dct):
        self.dct = dct

    def __str__(self):
        return str(self.dct)

    def key_exists(self, key):
        if not isinstance(key, (str, int, tuple)) or \
                key not in self.dct:
            raise KeyError(f'Ключа {key} не существует')
        return True

    def __getitem__(self, item):
        if self.key_exists(item):
            return self.dct[item]


    def __setitem__(self, key, value):
        if self.key_exists(key):
            self.dct[key] = value

    def __delitem__(self, key):
        if self.key_exists(key):
            del self.dct[key]