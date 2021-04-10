
def method(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0                                       #store hash value for pattern
    t = 0                                       #store hash value for text
    result = []

    for i in range(m):                         # To calculate the hash value of pattern   O(n)
        p = (d*p+ord(pattern[i]))%q             # and first window of the text          
        t = (d*t+ord(text[i]))%q                # ord is to find/return the unicode values    

    for s in range(n-m+1):                      # To check the current window of text      O(m)               
        if p == t:                              # each of them   
            match = True                        
            for i in range(m):                  #   
                if pattern[i] != text[s+i]:     #   
                    match = False
                    break
            if match:                           # 
                result = result + [s]           
        if s < n-m:                             # To calculate the hash value for next window of text   
            t = (t-(h*ord(text[s])))%q          # remove letter   
            t = (t*d+ord(text[s+m]))%q          # add letter    
            t = (t+q)%q                         # get positive value t >= 0    
    return result

text = input("Enter the text: ")
pattern = input("Enter the pattern: ")
d = 256
primenumber = 11
print (method (text, pattern, d, primenumber))