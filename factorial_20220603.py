#Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line.

def factorial_result(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    print(result)

factorial_result(0)