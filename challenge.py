def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    return total
def product_of_digits(num):
    total = 1

    while num > 0:
        digit = num % 10
        total *= digit
        num = num // 10

    return total

def reverse_number(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return reversed_num

def palindrem(num):
    if reverse_number(num) == num:
        return True
    else:
        return False

def find_largest_digit(num):
    largest = 0

    while num > 0:
        digit = num % 10
        if digit > largest:
            largest = digit
        num = num // 10

    return largest
def find_smallest_digit(num):
    smallest = 9

    while num > 0:
        digit = num % 10
        if digit < smallest:
            smallest = digit
        num = num // 10

    return smallest

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
def even_or_odd(num):
    even_count = 0
    odd_count = 0

    while num > 0:
        digit = num % 10

        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        num = num // 10

    return even_count, odd_count
number = int(input("Enter positive number: "))
even, odd = even_or_odd(number)

if number > 0:
    print(sum_of_digits(number))
    print(product_of_digits(number))
    print(reverse_number(number))
    print(palindrem(number))
    print(find_largest_digit(number))
    print(find_smallest_digit(number))
    print(factorial(number))
    print("Even digits:", even)
    print("Odd digits:", odd)
else:
    print("Please enter a positive number")