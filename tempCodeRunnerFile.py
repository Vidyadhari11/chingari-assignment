
def fib(devil_numbers,n):
    if n<=0:
        return "Number should be maximum"
    devil_numbers[0]=0
    devil_numbers[1]=1
    for i in range(2,n):
        devil_numbers[i]=devil_numbers[i-1]+devil_numbers[i-2]
    
    

def is_handsome_number(b):
    num_1,num_2=b[0],b[1]
    new_array=[]
    count=0
    for i in range(1,num_1+1):
        if num_1%i==0:
            new_array.append(i)

            count+=i
            
   
    length=len(new_array)
    #print(length)
    number=count%num_2
    devil_numbers=[0]*num_2
    fib(devil_numbers,num_2)
    #print(devil_numbers)