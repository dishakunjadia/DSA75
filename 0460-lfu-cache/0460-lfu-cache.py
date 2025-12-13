class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.key_table = {}
        self.freq_table = {}

    def _update_freq(self, node):
        freq = node.freq
        self.freq_table[freq].remove(node)

        # update minFreq
        if freq == self.minFreq and self.freq_table[freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        self.freq_table.setdefault(node.freq, DoublyLinkedList()).add_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1

        node = self.key_table[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_table:
            node = self.key_table[key]
            node.value = value
            self._update_freq(node)
            return

        if self.size == self.capacity:
            # evict LFU + LRU
            lfu_list = self.freq_table[self.minFreq]
            removed = lfu_list.remove_last()
            del self.key_table[removed.key]
            self.size -= 1

        # insert new key
        new_node = Node(key, value)
        self.key_table[key] = new_node
        self.freq_table.setdefault(1, DoublyLinkedList()).add_front(new_node)
        self.minFreq = 1
        self.size += 1


    
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)