# 1. Take two strings as input and concatenate them.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(str1 + str2)

# 2. Detect double spaces and replace with a single space.
text = input("Enter a string with double spaces: ")
print(text.replace("  ", " "))

# 3. Extract substring "Python".
text = "Welcome to Python Programming"
print(text[11:17])

# 4. Check palindrome and transform if not.
s = input("Enter a string: ").replace(" ", "").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Transformed palindrome:", s + s[::-1])

# 5. Input and print data type.
value = input("Enter something: ")
print("Data type is:", type(value))

# 6. Print pattern with escape sequences.
print("\"Python\"\nIs\nawesome!")

# 7. Count number of vowels in a string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

# 8. Replace all "a" with "@".
text = input("Enter a string: ")
print(text.replace('a', '@'))

# 9. Reverse a string using slicing.
text = input("Enter a string: ")
print(text[::-1])

# 10. Perform arithmetic operations on two numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

# 11. Count occurrence of each character.
text = input("Enter a string: ")
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# 12. Convert lowercase to uppercase and vice versa.
text = input("Enter a string: ")
print(text.swapcase())

# 13. Check if string is alphanumeric.
text = input("Enter a string: ")
print(text.isalnum())
