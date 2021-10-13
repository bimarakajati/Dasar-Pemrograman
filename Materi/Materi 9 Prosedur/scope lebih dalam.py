def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x,'\n')

def g(y):
    print(x)
    print(x + 1)
x = 5
g(x)
print(x,'\n')

def h(y):
    x += 1
x = 5
h(x)
print(x,'\n')