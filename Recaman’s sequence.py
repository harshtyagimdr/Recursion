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
    
def recaman(n): 
  
    
    arr = [0] * n 
  
    
    arr[0] = 0
    print(arr[0], end=" ") 
  
    
    for i in range(1, n): 
      
        curr = arr[i-1] - i 
        for j in range(0, i): 
          
            
            if ((arr[j] == curr) or curr < 0): 
                curr = arr[i-1] + i 
                break
              
        arr[i] = curr 
        print(arr[i], end=" ") 

if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        recaman(n)
        print()