#Create a list of your five favorite movies.
movies = ["Saaho", "Devara", "Dhebba Dhebba", "Salaar"]
print(movies)

#Print the first and last movie using indexing.
print(movies[0])
print(movies[-1])

#Add a new movie to the list.
movies.append("KGF")
print(movies)

#Change the third movie to something else.
movies[2] = "Avatar"
print(movies)

#Sort the list alphabetically.
movies.sort()
print(movies)

#Use append(), insert(), remove(), pop(), and reverse() on a sample list.
movies.append("Avengers")
print("After appending : ",movies)

movies.insert(1, "Mufasa")
print("After inserting : ",movies)

movies.remove("Devara")
print("After removing : ",movies)

movies.pop()
print("After pop : ",movies)

movies.reverse()
print("After reverse : ",movies)

#Print each element in the list using a for loop.
print("List of items : ")
for items in movies:
    print(items)

#Print only the movies that start with the letter “S”.
print("Movies starting with 's' : ")
for items in movies:
    if items[0].lower() == "s":
        print(items)

#Create a list of squares for numbers from 1 to 10.
numbersList= []
for numbers in range(1,11):
    numbersList.append(numbers ** 2)
print(numbersList)

#From a list of numbers, create a new list that contains only even numbers.
evenNumbersList = []
for evenNumbers in numbersList:
    if evenNumbers % 2 == 0:
        evenNumbersList.append(evenNumbers)
print(evenNumbersList)
