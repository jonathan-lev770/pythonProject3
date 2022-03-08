# call function with unpacking inside parameters, allows for more args to be passed when you call the function

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)


func1(10, 20, 1, 2, 3)  # extra args okay b/c of #c when defining function (comes out as tuple)
