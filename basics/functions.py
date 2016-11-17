def func(a=1, b=2, c=3):
    "This describes the function: a 'doctring'"  # a string inmediate after the def
    myVar = 'a string'   # local var
    global globalVar   # binds a local var globally
    globalVar = 'other string'  # a global var
    print(a + b + c)
    print(myVar)


def func2():
    print(globalVar)

func(3, b=4)
func2()


def addNum(num1, num2): return num1 + num2

result = addNum(3, 4)

print(result)

lamSum = lambda x, y: x + y

print(lamSum(2, 3))