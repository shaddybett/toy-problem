def solve(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    value = []
    alphabet_values = {char: idx + 1 for idx, char in enumerate('abcdefghijklmnopqrstuvwxyz')}

    current_consonant_value = 0
    max_consonant_value = 0

    for letter in word:
        if letter.lower() not in vowels:
            value.append(letter)
            current_consonant_value += alphabet_values[letter.lower()]
        else:
            # If a vowel is encountered, reset the current consonant value
            current_consonant_value = 0

        # Update the maximum consonant value
        max_consonant_value = max(max_consonant_value, current_consonant_value)

    return max_consonant_value

# Example usage:
result = solve('strength')
print(result)
