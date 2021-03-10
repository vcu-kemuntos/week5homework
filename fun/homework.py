"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    #magiclownumber= none
    #retval= magiclownumber
    #for  value in incoming_list:
        #if not retval:
            #retval = value
    #   if value> retvale
          #retval= value
    #return retval
    greatest_number = max(incoming_list)
    return greatest_number

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    least_number = min(incoming_list)
    return least_number


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    # summation=0
    if incoming_list:
       summation = sum(incoming_list)
    else:
        summation = 0
    return summation


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    if not incoming_dict:
        return None

    all_keys = incoming_dict.keys()
    if not all_keys:
        return None


    longest_value=None
    for key in all_keys:
        if not longest_value:
            longest_value= key


        if len(incoming_dict[key])>len(incoming_dict[longest_value]):
            longest_value=key
    return longest_value

