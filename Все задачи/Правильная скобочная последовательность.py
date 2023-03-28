def bracket_check(test_string):
    stack = []
    for el in test_string:
        if el == '(':
            stack.append('(')
        elif el == ')':
            if '(' in stack:
                stack.remove('(')
            else:
                print('NO')
                return
    if len(stack) > 0:
        print('NO')
    else:
        print('YES')

bracket_check("")