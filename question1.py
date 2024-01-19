a=int(input("Enter a number: "))
new_array=[]
for i in range(a):
    new_array_2=[]
    space=" "*(i+1)
    if i==0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        for j in range(1,a+1):
            new_array.append(str(j))
        string=" ".join(new_array)
        print(space+string)
    else:
        for k in range(1,a-i+1):
            total=int(new_array[k-1])+int(new_array[k])
            new_array_2.append(str(total))
        string=" ".join(new_array_2)
        new_array=new_array_2
        print(space+string)
