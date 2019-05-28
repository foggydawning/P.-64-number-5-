def s_f (number,i=1, k=0,sum=0):
    if number < 0:
        number*-1

    while number//10**i!=0:
        sum+=number%(10**i)//10**k
        i+=1
        k+=1
    sum+=number%(10**i)//10**k
    return sum

list=[]

list.sort(key = s_f, reverse = True )

print("Ваш отсортированный список:", list, sep="\n")
