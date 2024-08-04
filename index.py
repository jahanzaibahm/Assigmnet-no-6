# List
# Question: Write a function that takes a list of integers and returns the sum of all the elements in the list.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4])) 

# Tuple
# Question: Write a function that takes a tuple of numbers and returns the smallest number in the tuple.
def smallest_number(*numbers):
    return min(numbers)
print(smallest_number(* (1, 2, 3, 4)))




# Set
# Question: Write a function that takes a set of numbers and returns a new set with each element squared.
def set_numbers(*numbers):
    return {num**2 for num in numbers}

print(set_numbers(*{1, 2, 3}))


# Dictionary
# Question: Write a function that takes a dictionary and returns a list of all the keys in the dictionary.
def dic(person={
    "Name":"Jahanziab ahmed",
    "course":"Python",
    "Age":"18"
    
}):
    return list(person.keys())
print(dic())