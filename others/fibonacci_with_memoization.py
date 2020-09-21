'''
Memoization is the conceot of improving the efficiency of our code by caching pre-calculated values so they do not need to be re-calculated every time. 
'''
from time import perf_counter

class Fib:
  def __init__(self):
    self.cache = {1: 1, 2: 1}

  def fib(self, n):
    
    if n not in self.cache:
      #print(f'Calculating fib({n})')
      self.cache[n] = self.fib(n-1) + self.fib(n-2)
    elapsed = perf_counter() - start
    
    return self.cache[n]


f = Fib()
start = perf_counter()
print(f.fib(100))
elapsed = perf_counter() - start
print(f"Total time: {elapsed}")

print("\n-------------------------------\n")
print("Using closures")

def fib_2():
  cache = {1:1, 2:1}
  
  def calc_fib(n):
    if n not in cache:
      #print(f"Calculating fib({n})")
      cache[n] = calc_fib(n-1) + calc_fib(n-2)
    return cache[n]
  
  return calc_fib

f = fib_2()
start = perf_counter()
print(f(100))
elapsed = perf_counter() - start
print(f"Total time: {elapsed}")

print("\n-------------------------------\n")
print("Using decorators")

def memoize(fn):
  cache = dict()

  def inner(n):
    if n not in cache:
      cache[n] = fn(n)

    return cache[n]
  return inner

@memoize
def fib_3(n):
  return 1 if n<3 else fib_3(n-1) + fib_3(n-2)

start = perf_counter()
print(fib_3(100))
elapsed = perf_counter() - start
print(f"Total time: {elapsed}")


