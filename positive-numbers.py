def positive(a,b,c):
    numbers = [a,b,c]
    positive_numbers = []
    for number in numbers:
        if number % 2 == 0 and number > 0:
            positive_numbers.append(number)
    pos_numbers = len(positive_numbers)       
    if pos_numbers == 2:
        return True
    else:
        return False

result = positive(6,1,3)
print(result)