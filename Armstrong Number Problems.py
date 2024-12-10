
# write a program check Given Number Is Armstrong Or Not

n=int(input("Enter a number :"))
i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem**len(str(i))
        else:
            if c==i:
                k+=1
                print(i)
                if n==k:
                    break
    i+=1

# write a program Print Nth Armstrong  Number

n=int(input("Enter a number :"))
i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem**len(str(i))
        else:
            if c==i:
                k+=1
                if n==k:
                    print(i)
                    break
    i+=1

# write a program Print 10th Armstrong  Number

i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem**len(str(i))
        else:
            if c==i:
                k+=1
                if k==10:
                    print(i)
                    break
    i+=1

# write a program Print 5th To 10th Armstrong  Number

i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem**len(str(i))
        else:
            if c==i:
                k+=1
                if k>=5:
                    print(i)
                    if k==10:
                        break
    i+=1

