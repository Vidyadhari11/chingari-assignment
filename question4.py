        
                
def is_super_lucky_number(string):
    list_1=["1","2","3","5","6","8","9"]
    for i in string:
        if i in list_1:
            return False
    
    if len(string)==4 or len(string)==7:
        is_length_lucky_number=True
    else:
        is_length_lucky_number=False
    
    no_of_4_or_7=False
    count_of_7=string.count("7")
    count_of_4=string.count("4")
        
    if count_of_4==4 or count_of_4==7 or count_of_7==7 or count_of_7==7:
        no_of_4_or_7=True

    if is_length_lucky_number and no_of_4_or_7:
        return True
    else:
        return False



def is_super_lucky_palindrome(number):
    new_list=[]
    for i in range(1,10**18):
        string=str(i)
        reverse_string=string[::-1]
        is_palindrome=string==reverse_string
        super_lucky_number=is_super_lucky_number(string)
        if is_palindrome and super_lucky_number:
            new_list.append(i)
    return new_list[number]
        



a=int(input("Enter a number: "))
for i in range(a):
    b=int(input("enter a testcase number: "))
    result=is_super_lucky_palindrome(b)
    print(result)