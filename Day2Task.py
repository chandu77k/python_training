# 1. Reverse a string
original_text = "hello"
reversed_text = original_text[::-1]
print(reversed_text)

# 2. Check if a string is a palindrome
palindrome_candidate = "madam"
print(palindrome_candidate == palindrome_candidate[::-1])

# 3. Count vowels and consonants in a string
input_string = "Python"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for character in input_string:
    if character.isalpha():
        if character in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count, ", Consonants:", consonant_count)

# 4. Find the frequency of each character
char_input = "aabbcc"
char_frequency = {}
for character in char_input:
    if character in char_frequency:
        char_frequency[character] += 1
    else:
        char_frequency[character] = 1
print(char_frequency)

# 5. Remove all whitespaces from a string
text_with_spaces = " a b c "
text_no_spaces = text_with_spaces.replace(" ", "")
print(text_no_spaces)

# 6. Replace a word in a sentence
sentence = "I like Java"
updated_sentence = sentence.replace("Java", "Python")
print(updated_sentence)

# 7. Extract digits from a string
mixed_string = "abc123def"
extracted_digits = ''.join([char for char in mixed_string if char.isdigit()])
print(extracted_digits)

# 8. Check if a string contains only alphabets
alpha_check_string = "Hello123"
print(alpha_check_string.isalpha())

# 9. Capitalize the first letter of each word
lower_case_sentence = "hello world"
capitalized_sentence = lower_case_sentence.title()
print(capitalized_sentence)
