def has_duplicates(arr):
    
    max_value = max(arr)
    hash_table = [0] * (max_value + 1)


    for num in arr:
       
        if hash_table[num] == 1:
            return True
        
        hash_table[num] = 1

    
    return False


arr = [1, 2, 3, 1, 5]
print(has_duplicates(arr))  
