#Author: Saeed Alyami ssa5468@psu.edu

def digit_sum(n):
  n = int(n)
  if n > 0:
   return n%10 + digit_sum(n//10)
  else:
    return n 


def print_n(s,n):
  if n > 0:
    print (s)
    print_n(s,n//10)

def run():
  n = input ("Enter an int: ")
  n = int(n)
  print(f"sum of digits of {n} is {digit_sum(n)}.")
  

if __name__== "__main__":
  run()
