def who_are_you_and_hello():
    s = input()
    while s.count(" ") != 0 or s.capitalize() != s or not s.isalpha():
        s = input()
    print(f'Привет {s}')

who_are_you_and_hello()