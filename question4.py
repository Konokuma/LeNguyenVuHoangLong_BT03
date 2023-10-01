def are_anagrams(word1, word2):
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

   
    if len(word1) != len(word2):
        return False


    char_count1 = {}
    char_count2 = {}

    
    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

   
    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

   
    return char_count1 == char_count2


print(are_anagrams("restful", "fluster"))  
print(are_anagrams("hello", "world"))      
