def is_super_lucky_number(string):
    list_1=["1","2","3","5","6","8","9"]
    for i in string:
        if i in list_1:
            return False
    if len(string)==4 or len(string)==7:
        no_of_digits=True
    else:
        no_of_digits=False
    no_of_4_or_7=False
    for char in string:
        if i=="4" or i=="7":
            count=string.count(char)
            if count==4 or count==7:
                no_of_4_or_7=True
    if no_of_digits and no_of_4_or_7:
        return True
    else:
        return False
        
                




def is_super_lucky_palindrome(number):
    new_list=[]
    for i in range(1,10**18):
        string=str(i)
        reverse_string=string[::-1]
        is_palindrome=str(i)==reverse_string
        super_lucky_number=is_super_lucky_number(string)
        if is_palindrome and super_lucky_number:
            new_list.append(i)
    
    return new_list
        




a=int(input("Enter a number: "))
for i in range(a):
    b=int(input("enter a testcase number: "))
    result=is_super_lucky_palindrome(b)
    print(result)