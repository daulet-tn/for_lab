#1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)


print(multiply_list([2, 3, 4, 5]))  
#2
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

print(count_case("Hello World!"))  
#3
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))  
print(is_palindrome("hello"))  
#4
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Перевод миллисекунд в секунды
    return math.sqrt(number)

num = 25100
delay = 2123
print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")
#5
def all_true(tpl):
    return all(tpl)


print(all_true((True, True, 1, "Hello"))) 
print(all_true((True, False, 1))) 