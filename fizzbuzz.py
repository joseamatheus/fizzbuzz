

x=100
list_fb=[]
for i in range(1,x+1):
    list_fb.append(i)
    if i % 3 == 0 and i % 5 == 0:
        print ("Fizz Buzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)



    
    
print (list_fb)

