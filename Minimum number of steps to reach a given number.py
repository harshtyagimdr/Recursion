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
if __name__ == '__main__':
   
    for _ in range(int(input())) :
        n = int(input())
        sum=0
        flag=0
        i=1
        while True:
            sum+=i
            
            if sum==n:
                break
            if sum>n:
                flag=1
                break
            i+=1
        if flag:
            if (sum-n)%2==1:
                print(i+1)
            else:
                print(i)
        else:
            print(i)
                