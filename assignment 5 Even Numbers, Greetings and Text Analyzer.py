# TASK 1

def even_numbers(n):
    num = 2
    count = 0

    while count < n:
        yield num
        num += 2
        count += 1


# Decorator Function

def greet(func):
    def wrapper(name):
        print("Hello!")
        func(name)
    return wrapper


@greet
def introduce(name):
    print("My name is", name)


# Main Program

n = int(input("Enter how many even numbers you want: "))

print("Even Numbers:")

for number in even_numbers(n):
    print(number)

print()

introduce("Adith")

# output
# Enter how many even numbers you want: 3
# Even Numbers:
# 2
# 4
# 6

# Hello!
# My name is Adith

# TASK 2


import re

text = input("Enter text: ")

emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
print("Email Addresses:", emails)


phones = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}', text)
print("Phone Numbers:", phones)


old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

new_text = text.replace(old_word, new_word)

print("Updated Text:")
print(new_text)

# output
# Enter text: Email me at hello@example.com or admin@test.com
# Email Addresses: ['hello@example.com', 'admin@test.com']
# Phone Numbers: []
# Enter the word to replace: email
# Enter the new word: contact
# Updated Text:
# Email me at hello@example.com or admin@test.com