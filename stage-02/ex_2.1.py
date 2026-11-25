"""
	PREDICTION:
		In "A" the output will be:
			[1]
			[1, 2]
		In "B" the output will be:
			10
		In "C" the output will be:
			a
			None
		In "D" the output will be:
			8
		In "E" the output will be:
			UnboundLocalError: cannot access local variable ...

   I ran the code and found no difference from my prediction!
"""


# A
def add(x, lst=[]):
    lst.append(x)
    return lst
print(add(1)); print(add(2))

# B
x = 10
def f():
    x = 20
f()
print(x)

# C
def f():
    print("a")
r = f()
print(r)

# D
def g(a, b=2, *, c=3):
    return a + b + c
print(g(1, c=5))

# E
x = 1
def f():
    x = x + 1
    return x
print(f())
