def isPrime(num):
    for i in range(2,(num)):
        if(num%i==0):
            return False
    return True

for i in range(3,31):
    if(isPrime(i)):
        print(i)