def exponent_calc():
    
   
    
    Q1 = raw_input('What number would you like to add an exponent to?')
    Q2 = raw_input('What would you like the exponent be')
    
    if Q1.isalpha():
        print "Please type a number."
        exponent_calc()
        
    elif Q2.isalpha():
            print "Please type a number."
            exponent_calc()
    else:
        result = int(Q1)**int(Q2)
        print result
                
                
                
                
while (1):     
    Q = raw_input('Do a calculation?')
    if Q == "":
        break
    else: 
        exponent_calc();    
    
                
                


