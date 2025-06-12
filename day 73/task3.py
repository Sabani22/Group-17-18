def concat(numbers):
    str_numbers = [str(num) for num in numbers]
    result = '@'.join(str_numbers)
    return result

user_input = input("enter number ")
number_list = [int(x) for x in user_input.split()]
print(concat(number_list))