# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
   

# format_name("gago", "ka")

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     print(f"{formatted_f_name} {formatted_l_name}")

# format_name("gago", "ka")

def format_name(f_name, l_name):
    """Take a first and last name and format it
    return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))






# formatted_string = format_name("gago", "ka")
# print(formatted_string)
# print(format_name("gago", "ka"))
