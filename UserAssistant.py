import sys


# Get user first name and enforce char limit
def get_first_name():
    f_name_length = 0
    f_name = "Unknown"
    while f_name_length == 0 or f_name_length > 20:    # To enforce character limit
        f_name = input('First Name: ').capitalize()    # String Input with Method (Capitalize)
        f_name_length = len(f_name)                    # Len function to get string length
        if f_name_length > 20:
            print("Please use 20 characters or less.")
        elif f_name_length == 0:
            print("You must enter a name.")
    return f_name


# Get user last name and enforce char limit
def get_last_name():
    l_name_length = 0
    l_name = "Unknown"
    while l_name_length == 0 or l_name_length > 20:    # To enforce character limit
        l_name = input('Last Name: ').capitalize()     # String Input with Method (Capitalize)
        l_name_length = len(l_name)                    # Len function to get string length
        if l_name_length > 20:
            print("Please use 20 characters or less.")
        elif l_name_length == 0:
            print("Please enter your name to continue.")
    return l_name


# Get user age and ensure age is valid
def get_age():
    age = '0'       # String
    age_length = 0  # Integer
    while age_length == 0 or age_length > 3 or int(age, 10) <= 0 or int(age, 10) > 110:
        age = input('Age: ')    # String
        age_length = len(age)   # Integer
        if age_length == 0:
            print('Please enter your age to continue.')
        elif age_length > 3 or int(age, 10) <= 0 or int(age, 10) > 110:
            print('Please enter a valid age.')
    return int(age, 10)


def check_age(age):
    if age < 18:
        print("I'm sorry, but you are not old enough to use this service.")
        sys.exit()
    return


# -------------------------------------------------------------------------------
# Using strings with input, concatenation, character indexing, formatted strings, string methods, functions,
# type conversions
print("Hello, there! Before I can be of service to you, could you tell me your name?")
first_name = get_first_name()                                           # Get input and enforce char limit
first_initial = first_name[0].upper()                                   # String Method (Upper)
last_name = get_last_name()                                             # Get input and enforce char limit
last_initial = last_name[0].upper()                                     # String Method (Upper)
full_name = first_name + " " + last_name                                # Concatenation
full_initials = first_initial + last_initial                            # Concatenation
thank_you_msg = f'Thank you, {full_name}, or {full_initials}.'          # Formatted String
print(thank_you_msg)


print(f'Now, {first_name}, could you tell me your age?')
user_age = get_age()                                        # Get input and enforce char limit
check_age(user_age)                                         # Check and enforce age limit
