def converter(hour,minute,period):
    converted = []
    if 1 <= hour <= 12 and 0 <= minute <= 60 and period in ['AM','PM']:
        if period == 'AM':
            converted_hour = hour if hour != 12 else 0
        else:
            converted_hour = hour if hour == 12 else hour + 12
        time_str = f'{converted_hour:02d}{minute:02d}'
        return time_str                
        converted .append(f'{hour:02d}:{minute:02d}am')
        return converted
    else:
        return 'failed'
    

result = converter(1,5,'PM')
print(result)


