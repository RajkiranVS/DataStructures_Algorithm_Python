""""
Code to check whether the parentheses balance

balanced parentheses: {} {[]} ({[]})
unbalanced parentheses: { {[} [}
"""

from stack_implementation import Stack


def is_match(p_1, p_2):
    """
    Parameters
    ----------
    p_1: Top element pushed from Stack
    p_2: Next element in the string

    Returns
    -------
        True: If parentheses match
        False: If parentheses doesn't match
    """
    matching_parentheses = {"{": "}", "[": "]", "(": ")"}
    return bool(matching_parentheses[p_1] == p_2)


def is_parenthesis_balance(parentheses_string):
    """
    Parameters
    ----------
    parentheses_string: The input parentheses string

    Returns
    -------
    True: If balanced parentheses
    False: If unbalanced parentheses
    """
    stack_object = Stack()
    is_balanced = True
    index = 0

    while index < len(parentheses_string) and is_balanced:
        parentheses = parentheses_string[index]
        if parentheses in "({[":
            stack_object.push(parentheses)
        else:
            if stack_object.is_empty():
                is_balanced = False
            else:
                top = stack_object.pop()
                if not is_match(top, parentheses):
                    is_balanced = False
        index += 1
    return bool(stack_object.is_empty() and is_balanced)


print(is_parenthesis_balance("{[]}"))
