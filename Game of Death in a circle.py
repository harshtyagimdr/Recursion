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
def josephus(n,k):
    if n==1:
        return 1
    else:
        return (josephus(n-1,k)+k-1)%n+1
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n,k=(int(i) for i in input().split())
        print(josephus(n,k))
        