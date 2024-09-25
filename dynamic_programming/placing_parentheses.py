def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, operators, min_dp, max_dp):
    min_value = float('inf')
    max_value = float('-inf')
    
    for k in range(i, j):
        op = operators[k]
        a = evaluate(max_dp[i][k], max_dp[k+1][j], op)
        b = evaluate(max_dp[i][k], min_dp[k+1][j], op)
        c = evaluate(min_dp[i][k], max_dp[k+1][j], op)
        d = evaluate(min_dp[i][k], min_dp[k+1][j], op)
        
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
        
    return min_value, max_value

def maximum_value(dataset):
    # Clean the input by removing spaces and validating characters
    dataset = dataset.strip()
    if not dataset or not all(c.isdigit() or c in '+-*' for c in dataset):
        raise ValueError("Invalid input string")
    
    n = (len(dataset) + 1) // 2
    
    # Initializing min and max dp tables
    min_dp = [[0] * n for _ in range(n)]
    max_dp = [[0] * n for _ in range(n)]
    
    # Base case: when the expression is just a number
    for i in range(n):
        min_dp[i][i] = int(dataset[2 * i])
        max_dp[i][i] = int(dataset[2 * i])
    
    # Fill the tables for subexpressions of increasing length
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_dp[i][j], max_dp[i][j] = min_and_max(i, j, dataset[1::2], min_dp, max_dp)
    
    return max_dp[0][n-1]

if __name__ == "__main__":
    
        print(maximum_value(input("")))
    
