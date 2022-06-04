r'''
Date: 2022-05-28 17:01:33
LastEditors: Kunyang Xie
LastEditTime: 2022-05-29 17:30:46
'''
# taken from http://www.rosettacode.org/wiki/Tokenize_a_string_with_escaping


def token_with_escape_mutant1(inpt, escape="^", separator="|"):
    """
    Issue  python -m doctest thisfile.py  to run the doctests.

    >>> print(token_with_escape('one^|uno||three^^^^|four^^^|^cuatro|'))
    ['one|uno', '', 'three^^', 'four^|cuatro', '']
    """
    result = []
    token = ""
    state = 2
    # Change the state to 2, which will miss all the branches.
    for c in inpt:
        if state == 0:
            if c == escape:
                state = 1
            elif c == separator:
                result.append(token)
                token = ""
            else:
                token += c
        elif state == 1:
            token += c
            state = 0
    result.append(token)
    return result
