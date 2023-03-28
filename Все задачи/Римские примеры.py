def num_to_rim(num):
    nums = [
        ('M', 1000), 
        ("CM", 900), 
        ('D', 500), 
        ('CD', 400), 
        ('C', 100), 
        ('XC', 90), 
        ('L', 50), 
        ('XL', 40), 
        ('X', 10), 
        ('IX', 9), 
        ('V', 5), 
        ('IV', 4), 
        ('I', 1)
    ]
    
    result = ""
    for letter, weight in nums:
        while num >= weight:
            num -= weight
            result += letter
    return result




def roman():
    global one
    global two
    global three
    three = one + two
    print(f"{num_to_rim(one)} + {num_to_rim(two)} = {num_to_rim(three)}")


one = 5
two = 4
roman()
# def arab_to_roman( number ):
#     CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
#     if number <= 0: return ''
 
#     ret = ''
#     for arab, roman in CONV_TABLE:
#         while number >= arab:
#             ret += roman
#             number -= arab
 
#     return ret

# print(arab_to_roman(7))