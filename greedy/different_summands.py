def optimal_summands(n):
    summands = []
    sum=0
    i=1
    while sum<n:
        if sum+i<=n:
            summands.append(i)
            sum+=i
        else:
            summands[-1]+=n-sum
            break
        i+=1

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
