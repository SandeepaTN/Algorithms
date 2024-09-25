def compute_operations(n):
    if n == 1:
        return [1]
    
    minNumCoins = {1: [1]}

    for m in range(2, n + 1):
        min_steps = minNumCoins[m - 1] + [m]

        if m % 2 == 0:
            steps_via_2 = minNumCoins[m // 2] + [m]
            if len(steps_via_2) < len(min_steps):
                min_steps = steps_via_2

        if m % 3 == 0:
            steps_via_3 = minNumCoins[m // 3] + [m]
            if len(steps_via_3) < len(min_steps):
                min_steps = steps_via_3
        
        minNumCoins[m] = min_steps

    return minNumCoins[n]
            


    


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
