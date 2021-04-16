def isArmstrong(n):
    #ADD YOUR CODE HERE
       sum=0
       count=0
       temp=n
       a=n
       if(n<0):
         return False
       
       while n!=0:
          n=n//10
          count=count+1
  
       while a!=0:
          r=a%10
          sum=sum+(r**count)
          a=a//10
  
  
       if(temp==sum):
        return True
       else:
        return False
       if n < 0:
	return False
	
