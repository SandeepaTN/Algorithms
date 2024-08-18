def max_pairwise_product(numbers):
    n = len(numbers)
    max1=numbers[0]
    max2=0
    
    for i in range(1,n):
        if numbers[i]>=max1:
            max2=max1
            max1=numbers[i]
        elif numbers[i]>max2:
            max2=numbers[i]    
    return max1*max2        



if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
