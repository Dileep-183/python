i = int(input("Please Enter any Number: "))    
Reverse = 0    
while(i > 0):    
    Reminder = i %10    
    Reverse = (Reverse *10) + Reminder    
    i = i//10    
     
print("reverse " , Reverse)