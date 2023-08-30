numbers = [1, 2, 3, 4, 5]


def increment_numbers(numbers):
    new_numbers = []  # create an empty list to store the new numbers
    for number in numbers:
        new_numbers.append(number + 1)  # append the incremented value to the new list
    return new_numbers


if __name__ == '__main__':
    new_numbers = increment_numbers(numbers)
    print('Original numbers:', numbers)
    print('Incremented numbers:', new_numbers)
