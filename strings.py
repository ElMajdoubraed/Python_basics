print("""
 This is multiline text
 This is multiline text
""")
print('''
 This is multiline text
 This is multiline text
''')

print ("Hello " + "world" + "!")

print("Hello" * 5)

# THis is an escape sequence.
string = "This is a \"escape sequence\" python "
print(string)


# in and not
string = "python is the best programming language"
print('python' in string)
print('best' not in string)

# string indexing
string = "programming"
print(string[0])
print(name[-1])
print(name[1])

# string slicing
print(string[0:6]))
print(string[:6])
print(string[6:])

print(string[-1:-3])
print(name[-1:-4])

# string functions len, lower, upper, islower,isupper, captilize

print(len(string))
print(string.lower())
print(string.upper())
print(string.capitalize())
print(string.islower())
print(string.isupper())

Date = 1991
language="python"
print("Date of first version ", language, " is ", Date)
print(f'Date of first version {language} is {Date}')
