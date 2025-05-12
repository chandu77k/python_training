# 1. Count Word Frequencies
def count_word_frequencies():
    text = input("Enter a sentence : ")
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)

count_word_frequencies()

# 2. Merge Two Dictionaries
def merge_dicts():
    n1 = int(input("How many items in the first dictionary : "))
    dict1 = {}
    for _ in range(n1):
        key = input("Enter key: ")
        value = int(input("Enter value: "))
        dict1[key] = value

    n2 = int(input("How many items in the second dictionary : "))
    dict2 = {}
    for _ in range(n2):
        key = input("Enter key: ")
        value = int(input("Enter value: "))
        dict2[key] = value

    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value

    print(merged)

merge_dicts()

# 3. Invert a Dictionary
def invert_dictionary():
    n = int(input("How many items in the dictionary to invert : "))
    d = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        d[key] = value

    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]

    print(inverted)

invert_dictionary()

# 4. Most Frequent Value in a Dictionary
def most_frequent_value():
    n = int(input("How many name age pairs : "))
    d = {}
    for _ in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        d[name] = age

    value_count = {}
    for value in d.values():
        value_count[value] = value_count.get(value, 0) + 1

    most_common = max(value_count, key=value_count.get)
    print(most_common)

most_frequent_value()

# 5. Dictionary from Two Lists
def create_dict():
    n = int(input("Enter number of items for keys and values : "))
    keys = []
    values = []

    print("Enter keys:")
    for _ in range(n):
        keys.append(input())

    print("Enter values:")
    for _ in range(n):
        val = input()
        values.append(int(val) if val.isdigit() else val)

    result = dict(zip(keys, values))
    print(result)

create_dict()
