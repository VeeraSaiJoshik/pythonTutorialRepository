# type casting = it is when you convert a value from one datatype to another
# so you can type caste an int variable to string like this : 5 -> "5"

intValue = 1

floatValue = 2.0

stringValue = "3"

# to type caste a variable, you can simply using the format below:
# end_datatype(value_you_want_to_convert)
# so if I wanted to convert the string "3" to a int I can say : int("3")
# if I wanted to convert a float to a int, I can say : int(3.3) 
#   - NOTE : When you typecase from a float to an int, you ALWAYS round down

stringToInt = int("123")
stringToFloat = float("123.2")
intToFloat = float(123)
floatToInt = int(123.3)

print(stringToInt)
print(stringToFloat)
print(intToFloat)
print(floatToInt)