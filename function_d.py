def max_value(numbers):

    max_num = numbers[0]
    for number in numbers[1:0]:
        if number > max_num:
            max_num = number

    return max_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
