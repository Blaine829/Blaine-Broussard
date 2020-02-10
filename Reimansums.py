
import math
def reimann(f, a, b, type, n):
    dx=(b-a)/n
    x=0
    if type < 0:
        x=a
    elif type > 0:
        x = a + dx
    else:
        x = a + (dx/2)

    area = 0
    while x < b:
        y = f(x)
        area = area + y
        x = x + dx
    if type > 0:
        area = area + f(b)
    area = area * dx
    return area

def g(x):
    return (x*x-5*x+3)

def main():
    print(reimann(g,3,6,1,6))

if __name__ == '__main__':
    print(__name__)
    main()


