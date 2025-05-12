#Basic Set Operations:
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

#2. Set Membership:
def is_member(item, s):
    return item in s
print("3 in set1 : " ,is_member(3, set1))
print("6 in set2 : " ,is_member(6, set2))

#3. Removing Duplicates:
values = [1, 2, 2, 3, 4, 4, 5]
set3 = set(values)
print(set3)

#Take a sentence from user input and return a set of unique words (ignoring punctuation and case).
def sentence():
    inputSentence = str(input("Enter a sentence : "))
    inputSentence = inputSentence.lower()
    inputSentence = inputSentence.replace("."," ")
    inputSentence = inputSentence.replace(",", " ")
    inputSentence = inputSentence.replace("!", " ")
    inputSentence = inputSentence.replace("?", " ")
    inputSentence = inputSentence.split()
    uniqueWords = set(inputSentence)
    print(uniqueWords)
sentence()

#5. Given three sets of students who play football, basketball, and tennis, write a program to find:
football = {"Chandu", "Dhanush", "Sai"}
basketball = {"Chandu", "Dhanush"}
tennis = {"Chandu"}

all_three = football & basketball & tennis

only_football = football - basketball - tennis
only_basketball = basketball - football - tennis
only_tennis = tennis - football - basketball
only_one_sport = only_football | only_basketball | only_tennis

football_basketball = (football & basketball) - tennis
football_tennis = (football & tennis) - basketball
basketball_tennis = (basketball & tennis) - football
exactly_two_sports = football_basketball | football_tennis | basketball_tennis

print("Students who play all three sports:", all_three)
print("Students who play only one sport:", only_one_sport)
print("Students who play exactly two sports:", exactly_two_sports)
