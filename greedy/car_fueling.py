from sys import stdin


def min_refills(distance, tank, stops):
    c=0
    st=tank
    i=0
    if st>=distance:
            return c
    n=len(stops)
    while i<n:
        cc=i
        while  i<n and stops[i]<=st :
            i+=1
        if stops[i-1]>st:
            return -1
        
        if i==cc:
            return -1
        st=stops[i-1]+tank
        c+=1
        if st>=distance:
            return c

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
