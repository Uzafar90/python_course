# String data type

# literal assignment
first = "Utba"
last = "Zafar"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
pizza = str("Cheese")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a nubar to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was checking in.
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                               "
multiline += "                " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("U"))
print(first.endswith("Z"))

# Boolean data type
my_value = False
nice - bool(False)
print(type(nice))
print(isinstance(my_value, bool))

# Numeric data type
price = 100
nest_price = int(10)
print(type(price))
print(isinstance(best_price, bool))

gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in function for numbers
print(abs(gpa))

print(round(goa))
print(round(goa, 1))
