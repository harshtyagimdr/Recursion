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
    
def key(N):
    if N<= 6: 
        return N 
  
     
    maxi = 0
  
    for b in range(N-3, 0, -1): 
        curr =(N-b-1)*key(b) 
        if curr>maxi: 
            maxi = curr 
      
    return maxi
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        print(key(n))