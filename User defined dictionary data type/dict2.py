# Class for custom exception
class KeyNotFoundError(Exception):
    pass

class dict2:
    
    def __init__(self):
        self.size = 100
        self.hashmap = [[] for _ in range(100)]  # Initializing the hashmap size
    
    def hashing(self, key):
        hashed_key = hash(key) % self.size # Compute the hashed key by applying the modulus of the hash value of the key
        return hashed_key
    
    def insert(self, key, value):
        hash_key = self.hashing(key) #compute the hash key for the given key             
        key_exists = False #flag to check if the key already exists in the hashmap               
        slot = self.hashmap[hash_key] #get the slot (bucket) corresponding to the hash key        
        # Iterate over key-value pairs in the slot
        for i, kv in enumerate(slot):
            #unpack the key-value pair
            k, v = kv 
            #check if the key already exists in the slot
            if key == k:
                #if key exists, update its value and set flag to True
                key_exists = True
                break
        
        #if the key already exists in the hashmap
        if key_exists:
            #update the value associated with the key
            slot[i] = ((key, value))
        else:
            #append the new key-value pair to the slot
            slot.append((key, value))

            
    def get(self, key):
        hash_key = self.hashing(key) #compute the hash key for the given key
        slot = self.hashmap[hash_key] #get the slot (bucket) corresponding to the hash key
        # Iterate over key's in the slot
        for kv in slot:
            #unpack the key-value pair
            k, v = kv
            #check if the key already exists in the slot
            if key == k:
                #if the called key found returns the value
                return v
            else:
                #raising error
                raise KeyNotFoundError(f'Key "{key}" does not exist')
    
    def __setitem__(self, key, value): #method to insert a key-value pair using syntax similar to dictionary assignment (e.g., obj['a'] = 1)
        return self.insert(key, value)
    
    def __getitem__(self, key): # Method to retrieve the value associated with the given key (e.g., val = obj['a'])
        return self.get(key)
    
    def __iter__(self): # Method for iterating over keys in a for loop
        for slot in self.hashmap:
            for key, _ in slot:
                yield key # Produces each key from the hashmap one at a time
    
    def __str__(self):
        pairs = []
        for slot in self.hashmap:
            for key, value in slot:
                pairs.append(f'{key}: {value}')
        return '{' + ', '.join(pairs) + '}'
    

#Store key value pairs:    
obj=dict()

obj['a']=1
obj['b']=2
obj['c']=3

print(obj)

#. Access values based on a given key 
obj = dict2()
obj['a'] = 1
val = obj['a']
print(val)


#Throw a custom exception if the key used for accessing values

obj = dict2()
val = obj['a']

#Can be used in a for loop to get keys

for k in obj:
    print(f'key: {k}')