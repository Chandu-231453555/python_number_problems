
# write a program Check The Given No Is  Disarium Number Or Not

n=int(input("Enter a Number :"))
i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            c+=rem**len(str(dm))
            dm=dm//10
        else:
            if c==i:
                k+=1
                print(i)
                if n==k:
                    break
    i+=1
   
# write a program Print Nth Disarium Number

n=int(input("Enter a Number :"))
i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            c+=rem**len(str(dm))
            dm=dm//10
        else:
            if c==i:
                k+=1
                if n==k:
                    print(i)
                    break
    i+=1
# write a program Print 10th Disarium Number

i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            c+=rem**len(str(dm))
            dm=dm//10
        else:
            if c==i:
                k+=1
                if k==10:
                    print(i)
                    break
    i+=1
# write a program Print 5th To 10th Disarium Number

i=1
k=0
while True:
    if i>1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            c+=rem**len(str(dm))
            dm=dm//10
        else:
            if c==i:
                k+=1
                if k>=5:
                    print(i)
                    if k==10:
                        break
    i+=1
