user_message: str = "What is the capital of France?"

if user_message != "":
    print("user is allowed to send this message")
else:
    print("user is not allowed to send this message")

    
if "johnn" == "john":
    print("first condition is true")
elif "john" == "john":
    print("second condition is true")
else:
    print("both conditions are false")


name1 = "John"
name2 = "john"

if name1 != name2:
    print("Names are not equal")


if name1 == name2 and name1.lower() == name2.lower():
    print("First or second condition is true")
elif name1.lower() == name2.lower() and name1.upper() == name2.upper():
    print("Second condition is true")
elif name1.upper() == name2.upper():
    print("Third condition is true")
elif name1.title() == name2.title():
    print("Fourth condition is true")
else:
    print("Both conditions are false")
# The above code compares two names with case sensitivity and insensitivity.


text_var = "123a"
print(text_var.isnumeric())
