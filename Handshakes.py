import atexit
import io
import sys
#Contributed by :HARSH TYAGI
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
def catalanDP(n): 
      
    # Table to store results 
    # of subproblems  
    catalan = [1 for i in range(n + 1)] 
      
    # Fill entries in catalan[] 
    # using recursive formula  
    for i in range(2, n + 1): 
        catalan[i] = 0
        for j in range(i): 
            catalan[i] += (catalan[j] * 
                           catalan[i - j - 1]) 
    # Return last entry  
    return catalan[n] 
  
# Returns count of ways to connect 
# n points on a circle such that  
# no two connecting lines cross  
# each other and every point is 
# connected with one other point. 
def countWays(n): 
      
    # Throw error if n is odd  
    if (n & 1): 
        print("Invalid") 
        return 0
          
    # Else return n/2'th Catalan number 
    return catalanDP(n // 2) 
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        print(countWays(n))