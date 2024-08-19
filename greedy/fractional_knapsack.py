from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    net_value=[values[i]/weights[i] for i in range(len(values))]
    while capacity>0: 
        max_index=net_value.index(max(net_value))
        if capacity>=weights[max_index]:
            value+=values[max_index]
            capacity=capacity-weights[max_index]
            net_value[max_index]=0
            weights[max_index]=0
        else:
            value+=capacity*net_value[max_index]
            capacity=0    

    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
