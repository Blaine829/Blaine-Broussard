
import math
def newton(x):
     
     
     tolerance = 0.000001
     estimate = 1.0


     while True:
          estimate = (estimate + float(x) / estimate) / 2
          
          difference = abs(float(x) - estimate ** 2)
          if difference <= tolerance:
               return estimate

# Output the result
def main():
     
     while True:
          x = (input("Enter a positive number or enter/return to quit: "))
          if x == "":
               break
          estimate = newton(x)
     
          print("The program's estimate is", estimate)
          print("Python's estimate is     ", math.sqrt(float(x)))


if __name__ == '__main__':
    print(__name__)
    main()
assert(newton.newton(49) == 7.000000000000002)
assert(newton.newton(32) == 5.656854250817683)
assert(newton.newton(.5) == 0.7071067811873449)
