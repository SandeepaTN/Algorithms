from sys import stdin


def maximum_gold(capacity, weights):
    n=len(weights)
    m=capacity+1
    knap=[[0]*(m) for _ in range(n+1)]
    for i in range(0,n):
        for w in range(1,m):
            knap[i+1][w]=knap[i][w]
            if weights[i]<=w:
                val=knap[i][w-weights[i]]+weights[i]
                if knap[i+1][w]<val:
                     knap[i+1][w]=val
    return knap[i+1][w]
if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
