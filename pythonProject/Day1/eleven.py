a=int(input("Enter num"))
for i in range(2,a):
    if(a%i==0):
        print("Number is not prime")
        break
    else:
        print("Number is prime")
        break
