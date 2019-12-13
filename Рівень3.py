a= list(map(int,input("Введіть через кому послідовність цілих чисел :  ").split(",")))  

print("\n")
print("Список, який ми ввели :")
print(a)
N=1500				

fibs = [1, 1]

i=0
while True:

    fibs.append(fibs[i]+fibs[i+1])
    i=i+1
    if fibs[i+1]>N:
        break
print("Список чисел Фібоначчі :")
print(fibs)          
b=[]              
j=0
for j in range(len(a)):   
    k=0
    for k in range(len(fibs)-1):
        if a[j]!=fibs[k]:
            k=k+1
            continue
        else:
            b.append(a[j])
            break
print("Список, затребуваний в умові задачі : ")
print(b)
