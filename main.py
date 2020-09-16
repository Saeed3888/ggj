#Author: Saeed Alyami ssa5468@psu.edu
#Collaborator: Stanley Weiblinger skw5659@psu.edu
#Collaborator: Eric Byjoo ezb5481@psu.edu
#Collaborator: Kelly Chau kkc5558@psu.edu
#Section: 3
#Breakout: 3

def sum_n(n):
  if n <= 1:
    return 1 
  else:
    return n*sum_n(n-1)
def print_n(s, n):
  if n <= 0:
    return 0
  else:
    print(s)
    print_n(n-1)

def run():
  n=int(input(f"Enter an int:" ))
  print(sum_n(n))
  s= input(f"Enter a string: ")
  print(s) 

if __name__== "__main__":
  run()