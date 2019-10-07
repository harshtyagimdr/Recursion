def printPattern(n): 
  
    # Base case (When n becomes 0 or negative)  
    if (n == 0 or n < 0): 
        print(n, end = " ") 
        return
      
    # First print decreasing order 
    print(n, end = " ") 
    printPattern(n - 5) 
  
    # Then print increasing order 
    print(n, end = " ") 

t=int(input())
for i in range(t):
    n=int(input())
    printPattern(n)
    print()
    