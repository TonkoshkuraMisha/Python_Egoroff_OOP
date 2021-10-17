# Пример замыкания. Аналогичные действия могут производить экземпляры классов в ООП.
def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

