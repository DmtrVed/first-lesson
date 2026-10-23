def is_balanced(s):
    lst = list(s)
    if len(lst) == 1:
        return False
    if len(lst) == 0:
        return True
    for i in range(len(lst)//2):
        if (lst[i] == '(' and lst[-i-1] == ')') or (lst[i] == '[' and lst[-i-1] == ']') or (lst[i] == '{' and lst[-i-1] == '}'):
            return True
        else:
            return False
