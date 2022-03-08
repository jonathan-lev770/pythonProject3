def my_func(a, b):
    return a + b


# functions are objects so they have attributes (category, sub_cat)
my_func.category = 'math'
my_func.sub_category = 'arithmetic'
print(my_func.category)                       # match


# dir( )  will show available attributes for that function
print(dir(my_func(1, 2)))


