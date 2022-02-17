#simple make table
hash_table = list([i for i in range(10)])

#save hash

def storage_data(key, value):
    hash_address = hash(key)
    if hash_table[hash_address] != 0:
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][1]:
                return


#read hash
def read_data(key):
    hash_address = hash(key)
    return hash_table[hash_address]

    


