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
def printBin(s,one,zero,n):
    if one+zero==n:
        print(s,end=" ")
        return
    if one<n:
        printBin(s+'1',one+1,zero,n)
    if one>zero:
        printBin(s+'0',one,zero+1,n)
    
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        s=''
        printBin(s,0,0,n)
        print()