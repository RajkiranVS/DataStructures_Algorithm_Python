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
    if p_1 == "{" and p_2 == "}":
        return True
    elif p_1 == "(" and p_2 == ")":
        return True
    elif p_1 == "[" and p_2 == "]":
        return True
    else:
        return False


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
    if stack_object.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_parenthesis_balance("{]"))
