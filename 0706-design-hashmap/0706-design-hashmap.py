class MyHashMap:
    # options are to use a list with the index as they key. Based on constraints, need 1000000 indexes due to 1000000 values - lots of space, but then access will be O(1), put will be O(1), remove will be O(1) using hash function

    # option 2 - use list with 1000 indexes as there will be 1000 calls. Use node 

    def __init__(self):
        self.map = [[-1, -1] for _ in range(1000001)]
    
    def get_hash_value(self, key: int) -> int:
        return key % 1000001

    def put(self, key: int, value: int) -> None: # uses hashing and open addressing
        idx = self.get_hash_value(key) # use hash function to get idx
        if self.map[idx][0] == key:
            self.map[idx][1] = value
        else:
            self.map[idx] = [key, value] # add values

    def get(self, key: int) -> int:
        idx = self.get_hash_value(key)
        return self.map[idx][1]

    def remove(self, key: int) -> None:
        idx = self.get_hash_value(key)
        self.map[idx] = [-1, -1]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)