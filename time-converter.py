def converter(hour,minute):
    converted = []
    if 1 <= hour <= 12 and 0 <= minute <= 60 :
        converted .append(f'{hour}:{minute} am')
        return converted
    else:
        return 'failed'
    

result = converter(11,5)
print(result)


