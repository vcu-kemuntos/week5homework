"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """

    greatest_number=max(incoming_list)
    return greatest_number
def find_least_number(incoming_list):

    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    least_number=min(incoming_list)
    return least_number


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    added_numbers=sum(incoming_list)
    return added_numbers



def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """

    longest_key=len(max(incoming_dict,key=len))
    return longest_key


