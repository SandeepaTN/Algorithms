from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest=''
    numbers.sort(reverse=True)
    numbers.sort(key=lambda x:int(x[0]),reverse=True)
    
    for _ in range(len(numbers)):
        largest+=numbers[_]
    

    return int(largest)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
