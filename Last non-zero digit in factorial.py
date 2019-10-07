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
def fac(n):
    fact = 1
    
    for i in range(1,n+1): 
    	fact = fact * i 
    return fact
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        f=fac(n)
        f=str(f)
        for i in f[-1::-1]:
            if int(i) is not 0:
                print(i)
                break
            