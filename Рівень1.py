import random                                           
a=[round(random.random()*100,2) for i in range(25)]   
print("\n")                                         
print("Вихідний список :")   
print(a)                                          
a.sort()                                          
a.reverse()                                        
print("Список, відсортований за спаданням")  
print(a)                                         
b=a[1::2]                                  
print("Список елементів попереднього списку з непарними індексами")  
print(b)            