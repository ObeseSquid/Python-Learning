# ask user for name
name = input("what's your name?").strip().title(); # variable

# strings will be ignored when not assigned to variable - makeshift multiline comment
"""
# remove whitespace from input string
name = name.strip(); # strip removes from left and the right not inbetween

# captialise user input string
name = name.capitalize(); # capitalise first letter of input
name = name.title(); # capitalise first letter of all words

# remove whitepace and capitalise user input
name = name.strip().title();
"""
# print hello user
print("hello,", name, sep=" "); # sep is a parameter for formatting the seperation of items, it can be any string
# print(f"hello, {name}"); #alternative way