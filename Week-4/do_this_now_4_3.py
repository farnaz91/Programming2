"""
Write a for loop that prints Olympic years (every 4 years) from 1900 to now.
"""
for year in range(1900, 2021, 4):
    print("Olympics years", year)

"""
Write a function that returns the average value of a list of numbers passed in to it.
"""


def get_average(numbers):
    return sum(numbers) / len(numbers)


list_of_numbers = [1, 3, 4, 5]
print(get_average(list_of_numbers))
