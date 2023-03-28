name = "string value is a value of the string value"

stringLength = len(name)

# len() - the len function allows you to get how long a certain string is
print(stringLength)

# .find() - the .find() method allows you to get the index, starting from 0, of the first occurrence of a character of sequence of characters in a python program
# if the said character or sequence does not exist, then it returns -1
firstIndexOfN = name.find("n")
print(firstIndexOfN)

# .upper() - the upper case function allows you to make your entire string upper case
upperCaseString = name.upper()
print(upperCaseString)

# .capitalize() - the capitalize function capitalizes the first letter of a string
capitalizedString = "123".capitalize()
print(capitalizedString)

# .lower() - the lower case function allows you to make your entire string lower case
lowerCaseString = name.lower()
print(lowerCaseString)

numberList = ["123", "Hi my name is jo", "123 123", "123,123", "123.2", "1a1", " 123", "123 "]
for number in numberList:
    # the .isdigit() function checks if a given string is a number
    # it returns true if the given string contains and only containst he following characters : '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    # if you string has any other character it returns false
    print(number + " number status : " + str(number.isdigit()))
    
# the .isalpha() methods returns true if your string contains and only contains any of the alphabets(abcdefghijklmnopqrstuvwxyz)
# this method returns false if you use things such as spaces
print(name.isalnum())

# the .count() function returns how many occurences of a given substring occur in a string
print(name.count("string value"))

# the .replace(x, y) function takes inputs x and y. both x and y are strings
# the .replace function replaces all occurences of x in a string with y
print(name.replace("value", "length"))

# if you multiply a string by a number, it will repeat the string those many times
print((name + "\n")*3)