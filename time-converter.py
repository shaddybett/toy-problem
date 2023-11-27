def converter(hour,minute):
    converted = []
    if 1 <= hour <= 12 and 0 <= minute <= 60 :
        converted .append(f'{hour:02d}:{minute:02d}am')
        return converted
    else:
        return 'failed'
    

result = converter(11,5)
print(result)


