def is_prime(num):
    if num<=1:
        return False
    if num==2:
            return True
    i=2
    while  i<num: #we can modify this to divide the number till half the number so it csn reduce the compilling time 
        if num%i ==0:
            print(f"False {i}")
            return False
        i+=1
        
    return True
        
        
      
    #print("me")
        
    return True
number=int(input("Enter the Number:"))         
print(is_prime(number))
