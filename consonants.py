def words(letters):
    value = []
    vowels = ['a','e','i','o','u']
    for letter in letters:
        if letter.lower() not in vowels:
            value.append(letter)
        start_char = 'a'
        end_char = 'z'
        alphabet = [chr(char) for char in range(ord(start_char), ord(end_char) + 1)]  
        
        if value:
            last_letter = value[-1]
            index = alphabet.index(last_letter)
            return index
        else:
            return None
    
result = words('strength')
print(result)

