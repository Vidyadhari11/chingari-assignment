def get_proper_divisors_count(number):
        
        count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
                
        return count


def fib(devil_numbers,n):
    if n<=0:
        return "Number should be greater than 0"
    devil_numbers[0]=0
    devil_numbers[1]=1
    for i in range(2,n):
        devil_numbers[i]=devil_numbers[i-1]+devil_numbers[i-2]
    
    

def is_handsome_number(b):
    num_1,num_2=b[0],b[1]
    count=0
    for i in range(1,num_1+1):
        if num_1%i==0:
            count+=i
            
    number=count%num_2
    devil_numbers=[0]*num_2
    fib(devil_numbers,num_2)
    devil_count = get_proper_divisors_count(number)
    if devil_count in devil_numbers:
        return "YES."
    else:
        return "NO."

a=int(input("Enter a number: "))
for i in range(a):
    b=list(map(int,input("Enter a numbers: ").split()))
    result=is_handsome_number(b)
    print(result)

