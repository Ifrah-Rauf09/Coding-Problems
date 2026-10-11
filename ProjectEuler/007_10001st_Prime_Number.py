def prime_number():
    count=0
    num=1

    while count < 10001:
        num+=1

        for i in range(2, num):
            if num % i==0:
                break
        else:
            count+=1

    return num


print(prime_number())