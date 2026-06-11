text = input("Enter a string: ")

vowels_list = "aeiouAEIOU"

print("\n1. Consonants:")
consonants = ""

for char in text:
    if char.isalpha() and char not in vowels_list:
        consonants += char

print(" ", consonants)

print("\n2. Vowels:")
vowels = ""
for char in text:
    if char in vowels_list:
        vowels += char

print(" ", vowels)

print("\n3. Total number of characters:")
count = 0
for char in text:
    count += 1

print(" ", count)

print("4. Reversed string:")
reversed_str = ""

for i in range(count - 1, -1, -1):
    reversed_str += text[i]

print("", reversed_str)

print("\n" + "=" * 40)
