def edit_distance(first_string, second_string):
    
    n=len(first_string)
    m=len(second_string)
    distance=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 :
                distance[i][j]=j           
            if j==0 :
                distance[i][j]=i    
    for i in range(1,n+1):
        for j in range(1,m+1):
            d1,d2,d3=999,999,999
            
            d1=distance[i][j-1]+1
           
            d2=distance[i-1][j]+1   
            
            if first_string[i-1]==second_string[j-1]:
                    d3=distance[i-1][j-1]

            else:
                    d3=distance[i-1][j-1]+1
            distance[i][j]=min(d1,d2,d3)        
    return distance[i][j]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
