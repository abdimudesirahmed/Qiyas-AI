rows = 7

# Upper part
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Lower part
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

def myFun(*args, **kwargs):
    print("non-keyword arguments (*args_):")
    for arg in args:
        print(arg)
    print("\nkeyword arguments (**kwargs_):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun("Hey", "Welcome", first="python", mid="for", last="pythons")

def evenOdd(a):
    if a%2 == 0:
        print(a**2)
    else:
        print(a**3)

evenOdd(2)
evenOdd(3)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(9))


def  sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return n+sumOfDigits(n-1)

print(sumOfDigits(10))


value_range = range(0, 10)
result = [value**2 if value % 2 == 0 else value**3 for value in value_range]

print(result)


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [value for row in mat for value in row]
print(res)

func =[lambda ard=x:ard*10 for x in range(1, 5 )]

for i in func:print(i())
