def is_valid_parenthesis(s):
    dicit = {
        '(': ')',
          "{": "}",
         '[': ']'

    }
    stack = []
    for i in stack:
        if i in dicit.keys(): stack.append(i)
        else:
            if len(stack) == 0:
                return False
            

            op = stack.pop()
            if dicit[op] != i:
                return False
    if len(stack) != 0:
        return False
    
    return True