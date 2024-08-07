def format_name(f_name, l_name):
    """This function requests First and Last name and returns it in a formated title line"""
    #f_name is the First name
    #l_name is the Last name
    formated_name = f_name.title()
    formated_last = l_name.title()
    return f"{formated_name} {formated_last}"
    
print(format_name("anton", "KHEIFETS"))

