def binary_search(keys, query):
    # write your code here
    high=len(keys)-1
    low=0
    res=-1
    while low<=high:
        mid=(high+low)//2
        
        if query==keys[mid]:
            res= mid
            high=mid-1
            
        elif keys[mid]<query:
            low=mid+1
        else:
            high=mid-1
    return res


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
