# "1. Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, 
# and would like to greet him slightly differently. She added a special case in her function, b
# ut she made a mistake.
# Can you help her?
# Examples
# "Matt"➞ "Hello, Matt!"
# "Helen" ➞ "Hello, Helen!"
# "Mubashir" ➞ "Hello, my Love!""

name = input("Please enter yor name>")
text= (name == "Mutabish") * "Hello my love!" or ("Hello"+" " + name+ "!")


# "2. Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
# Examples
# a,b = 9, 10 ➞ True
# a,b = 9, 9 ➞ False
# a,b = 1, 9 ➞ True"

def make_number(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    return False

example= make_number(1, 9)

a,b = 2,9
text=((a+b== 10) or (b == 10) or (a==10)) * "True" or "False"

# 3 " Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.
# Examples
# 5 ➞ True
# -55 ➞ True
# 37 ➞ False"

x=78
y= x % 5 
text= ("Thrue" * (y == 0)) or "False" 

# "4. Extra Knowledge 
# Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# Examples
# "AB", "CD" ➞ True
# "ABC", "DE" ➞ False
# "hello", "edabit" ➞ False"

x= "AB"
y= "CD"
text= (len(x) == len(y)) * "True" or "False"

# "5. Given a string, return True if its length is even or False if the length is odd."

x= "ABCD"
y= (len(x) % 2)
text=(y==0) * "Zuyg"  or "Kent" 
# "6. Create a function that takes a string txt and a number n and returns the repeated string n number of times.
# If given argument txt is not a string, return Not A String !!
# Examples
# "Mubashir", 2 ➞ "MubashirMubashir"
# "Matt", 3 ➞ "MattMattMatt"
# 1990, 7 ➞ "Not A String !!""

name, repeat= "Mubashir", 3
text= ((type(name) != str) * "Not a String") or  (name * repeat)












