# write a program to given number is prime number or not

no=int(input("Enter Your Number :"))
for i in range(2,no//2+1):
    if no%i==0:
        print("Given No is Not A Prime No:-",no)
        break  
else:
    print("Given No is Prime No:-",no)


# write a program to print nth prime Number 

count=int(input("Enter how many prime no u want :"))
a=1
pm_co=0
while True:
    if a>=1:
        for i in range(2,a//2+1):
            if a%i==0:
                break
        else:
            pm_co+=1
            if pm_co==count:
                print(a)
                break
        a+=1


# write a program to print 10th prime Numbers

a=1
pm_co=0
while True:
    if a>=1:
        for i in range(2,a//2+1):
            if a%i==0:
                break
        else:
            pm_co+=1
            print(a)
            if pm_co==10:
                break
        a+=1

# write a program to print 5th  To 10th prime Numbers 

a=1
pm_co=0
while True:
    if a>=1:
        for i in range(2,a//2+1):
            if a%i==0:
                break
        else:
            pm_co+=1
            if pm_co>=5:
                print(a)
                if pm_co==10:
                    break
    a+=1

