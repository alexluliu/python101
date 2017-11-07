#sumxy.py 
import sys

def sumxy(x, y):
    return x + y

if __name__ == '__main__':
    args = sys.argv[1:]
    x = float(args[0])
    y = float(args[1])
    print sumxy(x, y)