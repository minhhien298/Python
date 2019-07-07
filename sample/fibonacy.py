def fib2(n: int) -> int:
 if n < 2: # base case
  return n
 return fib2(n - 2) + fib2(n - 1) # recursive case

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # our base cases
def fib3(n: int) -> int:
 if n not in memo:
  memo[n] = fib3(n - 1) + fib3(n - 2) # memoization
 return memo[n]

from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n: int) -> int: # same definition as fib2()
 if n < 2: # base case
  return n
 return fib4(n - 2) + fib4(n - 1) # recursive case

def fib5(n: int) -> int:
 if n == 0: return n # special case
 last: int = 0 # initially set to fib(0)
 next: int = 1 # initially set to fib(1)
 for _ in range(1, n):
  last, next = next, last + next
 return next

if __name__ == "__main__":

 print(fib5(10))

 xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

 print(sorted(xs.items(), key=lambda x: x[1]))