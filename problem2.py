#2. User Input Data Processor

#Task 1: Input Length Validator
def input_length_validator(input_string):
    return len(input_string) >= 2
#end function

def validate_name(first_name, last_name):
    first_is_valid = input_length_validator(first_name)
    last_is_valid = input_length_validator(last_name)
    
    if first_is_valid and last_is_valid:
        return "Both names are valid."
    elif first_is_valid and not last_is_valid:
        return "Last name is not valid."
    elif not first_is_valid and last_is_valid:
        return "First name is not valid."
    else:
        return "Neither name is valid."
    #end if
#end function

def get_name_from_user():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    
    return first_name, last_name
#end function

first_name, last_name = get_name_from_user()
print(validate_name(first_name, last_name))