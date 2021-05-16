def biggie_size(lis):
    for x in range(0,len(lis)-1,1):
        if x > 0 :
            lis[x] = "big"
    return lis
print(biggie_size([- 1,3,5,-2]))

def count_positives(lis):
    counter = 0
    for x in range(0,len(lis),1):
        if lis[x] > 0:
            counter = counter + 1
    lis[len(lis)-1] = counter
    return lis
print(count_positives([-1,1,1,1]))

def sum_total(lis):
    sum =0
    for x in range(0,len(lis),1):
        sum = sum+lis[x]
    return sum
print(sum_total([1,2,3,4])) 

def average(lis):
    sum = 0
    avg = 0
    for x in range(0,len(lis),1):
        sum = sum + lis[x]
    avg = sum / len(lis)
    return avg
print(average([1,2,3,4]))

def length(lis):
    return len(lis)
print(length([37,2,1,-9]))


def minimum (lis):
    min = lis[0]
    for x in range(1,len(lis),1):
        if lis[x] < min:
            min = lis[x]
    if len(lis) == 0:
        return False
    else: return min
print(minimum([37,2,1,-9]))

def maximum (lis):
    max = lis[0]
    for x in range(1,len(lis),1):
        if lis[x] > max:
            max = lis[x]
    if len(lis) == 0:
        return False
    else: return max
print(maximum([37,2,1,-9]))

def ultimate_analysis(lis):
    sum = 0
    avg = 0
    min = lis[0]
    max = lis[0]
    for x in range(0,len(lis) , 1):
        sum = sum +lis[x]
        if lis[x]<min :
            min = lis [x]
        if lis[x] > max:
            max = lis[x]
    avg = sum / len(lis)
    new = "'sumTotal :', {} , 'Average :', {}, 'minimum :',  {},'Maximum :', {} , 'length', {}".format(sum,avg,min,max,len(lis))
    return new
print(ultimate_analysis([37,2,1,-9]))

def reverse(lis):
    lis = lis[::-1]
    return lis
print(reverse([37,2,1,-9]))



class car :
    def __init__(self, name , colore):
        self.name = name
        self.colore = colore


class vw (car):
    pass



golf = vw("golf" , "red")
print(golf.name,golf.colore)
x = car("lion","1990")
print(x.model , x.date)


