import random            

md = [0, 0, 0]        

md[0] = random.randint(0, 100)  
md[1] = random.randint(0, 100)
while md[1] == md[0]:               
    md[1] = random.randint(0, 100)
md[2] = random.randint(0, 100)
while (md[2] == md[0]) and (md[2] == md[1]) : 
    md[2] = random.randint(0, 100)
for i in md:          
    print(i)

 
