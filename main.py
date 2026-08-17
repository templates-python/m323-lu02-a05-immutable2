"""Listen.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu02/aufgaben/immutable2
"""

SAMPLE_NUMBERS = [1, 2, 3, 4, 5]


def increment_numbers(numbers):
    new_numbers = []  # create an empty list to store the new numbers
    for number in numbers:
        new_numbers.append(number + 1)  # append the incremented value to the new list
    return new_numbers


if __name__ == '__main__':
    demo_new_numbers = increment_numbers(SAMPLE_NUMBERS)
    print('Original numbers:', SAMPLE_NUMBERS)
    print('Incremented numbers:', demo_new_numbers)
