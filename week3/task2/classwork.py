# def multiply(a,b):
#     return a + b

# print(multiply(2,5))     

# def welcome(name, surname):
#     return f"Hello {name="John"}  {surname="Conor"}"

# welcome()

# def keyword_function(key=1, key_two=2):
#     return key + key_two

# print(keyword_function(key=5, key_two=4))    

# def create_profile(name, age, image="default.jpg"):
#     return name, age, image
# print(create_profile(name='Asan', age=20, image='2.jpg'))    

# def mixed_function(a, b=2, c=3):
#     return a + b + c
# print(mixed_function(0))

# def foo(required, *args, **kwargs):
#     print(required)
#     if args:
#         print(args)
#     else:
#         print(kwargs)    

# foo('Hello', key='Value1', key2='99999')

# def many(*args, **kwargs):
#     print(args)
#     print(**kwargs)

# many(1,2,3, name='Mike', job='Python develop

# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n * factorial(n-1) 

# print(factorial(5))       
# 
def Fib(n):
    if n <=1:
        return n
    else:
        return Fib(n-1) + Fib(n-2) 
print(Fib(9))              