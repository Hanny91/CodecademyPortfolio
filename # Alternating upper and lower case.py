# Prints a string alternating upper and lower case characters
string = "Today is going to be a good day"
string_list = list(string)

for char in range(len(string_list)):
    if char % 2 == 0:
        string_list[char] = string_list[char].upper()

string_list = "".join(string_list)
print(string_list)

# Prints a string alternating upper and lower case words
string = "And tomorrow we'll smash it too"
string_list = string.split()

for word in range(len(string_list)):
    if word % 2 == 0:
        string_list[word] = string_list[word].upper()
string_list = " ".join(string_list)
print(string_list)

