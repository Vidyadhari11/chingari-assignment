def get_total_prime_number_count(number):
    if number<=2:
        return 0
    prime_count=0
    for i in range(2,number):
        count=0
        
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            prime_count+=1
    return prime_count


a=int(input("Enter a number: "))
for i in range(a):
    b=int(input("Enter a testcase number: "))
    result=get_total_prime_number_count(b)
    print(result)