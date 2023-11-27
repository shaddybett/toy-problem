def words(letters):
    value = []
    vowels = ['a','e','i','o','u']
    for letter in letters:
        if letter.lower() not in vowels:
            value.append(letter)
    return value
    
result = words('hello')
print(result)
