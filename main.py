#Author: Saeed Alyami ssa5468@psu.edu
#Collaborator: Stanley Weiblinger skw5659@psu.edu
#Collaborator: Eric Byjoo ezb5481@psu.edu
#Collaborator: Kelly Chau kkc5558@psu.edu
#Section: 3
#Breakout: 3

def sum_n(n):
  n = int(n)
  if n > 0:
   return n+sum_n(n-1)
  else:
    return n 


def print_n(s,n):
  if n > 0:
    print (s)
    print_n(s,n-1)

def run():
  n=input ("Enter an int: ")
  n=int(n)
  print(f"sum is {sum_n(n)}.")
  s = input(f"Enter a string: ")
  print_n(s,n)

if __name__== "__main__":
  run()
