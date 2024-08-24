from functools import cmp_to_key

def custom_compare(x, y):
   
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    
    if not numbers:
        return "0"

    
    sorted_numbers = sorted(numbers, key=cmp_to_key(custom_compare))
    
    
    if sorted_numbers[0] == "0":
        return "0"

 
    largest = ''.join(sorted_numbers)
    
    return largest

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
