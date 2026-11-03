class LRUCache:

    def __init__(self, capacity: int):
        #we can use an ordered dict
        self.store = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.store:
            self.store.move_to_end(key) #move to end as recently accessed
            return self.store[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        #must first determine if key exists already
        if key in self.store:
            self.store[key] = value 
            self.store.move_to_end(key) #move to end

        #must next determine if reached capacity
        elif len(self.store) >= self.capacity: 
            #must remove least used; which should be the first in the ordered dict
            self.store.popitem(last=False)
            self.store[key] = value

        else: #simply add
            self.store[key] = value
        
