def max_value(numbers):
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    
    return max_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
