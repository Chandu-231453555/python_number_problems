
# write a program to Given Number Is Harshad (OR) Niven Or Not

n=int(input("Enter a nnumber :"))
i=1
k=0
while True:
    if i>=1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem
        else:

            if i%c==0:
                k+=1
                print(i)
                if n==k:
                    break
    i+=1


# write a program to Prinnt Nth Harshad (OR) Niven Number

n=int(input("Enter a nnumber :"))
i=1
k=0
while True:
    if i>=1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem
        else:

            if i%c==0:
                k+=1
                if n==k:
                    print(i)
                    break
    i+=1

# write a program to Prinnt 10th Harshad (OR) Niven Number

i=1
k=0
while True:
    if i>=1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem
        else:

            if i%c==0:
                k+=1
                if k==10:
                    print(i)
                    break
    i+=1

# write a program to Prinnt 5th To 10th Harshad (OR) Niven Number

i=1
k=0
while True:
    if i>=1:
        dm=i
        c=0
        while dm>0:
            rem=dm%10
            dm=dm//10
            c+=rem
        else:

            if i%c==0:
                k+=1
                if k>=5:
                    print(i)
                    if k==10:
                        break
    i+=1

