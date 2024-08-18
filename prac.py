def mi(a):
    
    a.sort()
    n=len(a)
    eq=round(sum(a)/len(a))
    
    dif=[0]*len(a)
    for i in range (len(a)):
      dif[i]=eq-a[i]
    co=dif[-1] 
   
    cost=abs(dif[-1])
    for i in range (n-2,-1,-1):
      if a[i]!=[i+1]:     
       
        dif[i]-=co
        co+=dif[i]
        
        cost+=abs(dif[i])
        print(dif)
        print(cost)
            
        
    for i in range(n):
       a[i]=a[i]+dif[i]
              
            
          
        
    return  cost          
       



a=[1,2,1,5]
print(mi(a))
print(a)

-2,-2,-1,2

