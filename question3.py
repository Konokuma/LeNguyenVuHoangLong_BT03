def reverse_integer(x):
   
    if x < 0:
        sign = -1
        x = abs(x)
    else:
        sign = 1

    reversed_str = str(x)[::-1]  
    reversed_int = int(reversed_str) 

  
    reversed_int *= sign


    if reversed_int < -2**31 or reversed_int > 2**31 - 1:
        return 0  

    return reversed_int


print(reverse_integer(1234))  
