def generate_next_fib(a, b, c):
  a = b
  b = c
  c = a + b
  return a, b, c

a=0
b=1
c=1
gr=0

while gr != 1.61803398875:
  a,b,c = generate_next_fib(a,b,c)
  gr = round(c/b, 11)
  print(f'{b} {c} {gr}')
