def HashFunc(key):
    sum = 0
    for i in range(len(key)):
        sum += ord(key[i]) * (i + 1)
    return sum

class HashTableNode:
    def __init__(self, val, key):
        self.value = val
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, size):
        self.hashtable = [None] * size
        self.size = size

    def Insert(self, key, value):
        index = HashFunc(key) % self.size

        if self.hashtable[index] is None:
            self.hashtable[index] = HashTableNode(value, key)
        else:
            current = self.hashtable[index]
            if current.key == key:
                current.value = value
                return
            else:
                while current.next != None:
                    if current.key == key:
                        current.value = value
                        return
                    current = current.next
                current.next = HashTableNode(value, key)

    def Search(self, key):
        index = HashFunc(key) % self.size

        if self.hashtable[index] is None:
            return None
        else:
            current = self.hashtable[index]
            while current != None:
                if current.key == key:
                    return current.value
                current = current.next
            return None

if __name__ == "__main__":
    ht = HashTable(27)

    ht.Insert("abc", 50)
    ht.Insert("john", "blue")
    ht.Insert("cow", 321312)

    print(ht.Search("abc"))
    print(ht.Search("john"))

    ht.Insert("abc", 70)

    print(ht.Search("abc"))

    print(ht.Search("nam"))