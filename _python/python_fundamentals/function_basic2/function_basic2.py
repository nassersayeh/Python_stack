def countdown(a):
    new_list = []
    for x in range(a,-1,-1):
        new_list.append(x)
    return new_list
print(countdown(5))

def print_and_return(lis):
    for x in range(0,len(lis),1):
        print(lis[0])
        return lis[1]
print_and_return([1,2])


def first_plus_length(lis):
    sum = lis[0]+len(lis)
    return sum 
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(lis):
    new_lis = []
    for x in range(0,len(lis),1):
        if lis[x]>lis[1]:
            new_lis.append(lis[x])
    print(len(new_lis))
    if len(new_lis)<2:
        return False
    else: return new_lis

print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(size,value):
    new_lis = []
    for x in range(0,size,1):
        new_lis.append(value)
    return new_lis
print(length_and_value(4, 7))