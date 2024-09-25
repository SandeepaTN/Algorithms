from itertools import combinations
number_of_inversions = 0
def merge(b,c):
    p=len(b)
    q=len(c)
    d=[]
    while len(b) and len(c):
        global number_of_inversions
        b1=b[0]
        c1=c[0]
        if b1<=c1:
            d.append(b[0])
            del b[0]
        else:
            d.append(c1)
            del c[0]

            number_of_inversions += len(b)
    while  len(b) >0:
        d.append(b[0])
        del b[0]
    while  len(c) >0:
        d.append(c[0])
        del c[0]
    return d




def mergeSort(a):
    n=len(a)
    if n<2:
        return a
    m=n//2
    b=mergeSort(a[:m])
    
    c=mergeSort(a[m:])
    
    a1=merge(b,c)
    
    return a1

def inversions_naive(a):
    n=len(a)
    mergeSort(a)
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
