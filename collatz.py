def getCollatzSequence(x):
    a=[]
    if x<0:
      return a
    elif x>0:
      a.append(x)
      while x!=1:
        if(x%2==0):
          x=x//2
          a.append(x)
        else:
          x=((x*3)+1)
          a.append(x)
    return a
 
