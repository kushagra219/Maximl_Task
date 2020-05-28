def smallesteSubstr_maxDistictChar(str): 
  
    n = len(str)   
 
    max_distinct = len(set(str)) 
    minl = n  

    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = len(set(subs)) 
              
            if (subs_lenght < minl and 
                max_distinct == sub_distinct_char): 
                minl = subs_lenght 
  
    return minl 

if __name__ == "__main__":  
    str = input()  
    l = smallesteSubstr_maxDistictChar(str)
    print(l) 

 