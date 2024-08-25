from random import randint


def partition3(array, left, right):
    pivot=array[left]
    j=left
    count=0
    for i in range(left+1,right+1):
        if array[i]<=pivot:
            if array[i]==pivot:
                count+=1
            j=j+1
            array[j],array[i]=array[i],array[j]
        
    array[j],array[left]=array[left],array[j]
       
        
    m=j
    i=m-1
    while count>0:


        if array[i]==pivot:
            m=m-1
            array[m],array[i]=array[i],array[m]
            count-=1
        i-=1    

    

    return m,j



def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    if input_n>0:
        elements = list(map(int, input().split()))
        assert len(elements) == input_n
        randomized_quick_sort(elements, 0, len(elements) - 1)
        print(*elements)
