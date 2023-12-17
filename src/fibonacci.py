
def fibonacci(num : int):
    num1, num2= 0,1
    for i in range(num):
        yield num1
        num1, num2 = num2, num1 + num2
         

# Using the generator
fib_gen = fibonacci(8)
print(list(fib_gen))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
