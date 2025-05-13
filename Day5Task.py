# 1. Match Statement – Day of the Week
day = int(input("Enter day number (1–7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# 2. For Loop – Multiplication Table
number = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 3. While Loop – Number Guessing Game
import random
target = random.randint(1, 100)
guess = -1
attempts = 0
while guess != target:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")


# 4. Function – Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [str(i) for i in range(1, 101) if is_prime(i)]
print("Prime numbers between 1 and 100:", ", ".join(primes))


# 5. Lambda – Sorting a List of Tuples
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sorted(people, key=lambda x: x[1])
print("Sorted by age:", sorted_people)


# 6. Arrays – Reverse an Array
original_array = [1, 2, 3, 4, 5]
reversed_array = original_array[::-1]
print("Original array:", original_array)
print("Reversed array:", reversed_array)


# 7. Class and Object – Bank Account
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"Current balance: ${self.balance}")

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.get_balance()


# 8. For Loop – Fibonacci Series
n = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=", ")
    a, b = b, a + b


# 9. While Loop – Factorial Calculation
number = int(input("Enter a number to calculate factorial: "))
fact = 1
temp = number
while temp > 1:
    fact *= temp
    temp -= 1
print(f"Factorial of {number} is {fact}")


# 10. Function – Palindrome Checker
def is_palindrome(s):
    return s == s[::-1]

strings = ["radar", "hello", "level", "world"]
for word in strings:
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
