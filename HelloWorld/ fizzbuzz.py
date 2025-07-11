# Classic interview question
# Rules:
# 1)  If input divisible by 3, return string "Fizz"
# 2)  If input divisible by 5, return string "Buzz"
# 3)  If input divisible by 3 & 5, return string "FizzBuzz"
# 4)  Otherwise, return the input

def fizz_buzz(input):
    if (input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"

    return input


print(fizz_buzz(3))
